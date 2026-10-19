"""Build visible breadcrumbs and matching JSON-LD from the MkDocs navigation."""

import json


ROOT_URL = "https://soroush-zendedel.github.io"
ROOT_LABEL = "خانه"


def _find_page_path(items, target_url, parents=()):
    for item in items:
        if getattr(item, "is_page", False):
            if item.url == target_url:
                return parents
        elif getattr(item, "is_section", False):
            found = _find_page_path(
                item.children, target_url, parents + (item.title,)
            )
            if found is not None:
                return found
    return None


def on_page_context(context, page, config, **kwargs):
    """Expose a single breadcrumb model to both HTML and JSON-LD templates."""
    if page.url in ("", "index.html"):
        context["seo_breadcrumbs"] = []
        context["seo_breadcrumb_json"] = ""
        return context

    site_url = config.site_url
    trail = [{"name": ROOT_LABEL, "url": ROOT_URL}]
    trail.append({"name": config.site_name, "url": site_url})

    nav = context.get("nav")
    section_titles = _find_page_path(nav.items, page.url) if nav else None
    if section_titles:
        trail.extend({"name": title, "url": None} for title in section_titles)

    trail.append({"name": page.title, "url": None})
    items = []
    for position, crumb in enumerate(trail, start=1):
        item = {
            "@type": "ListItem",
            "position": position,
            "name": crumb["name"],
        }
        if crumb["url"]:
            item["item"] = crumb["url"]
        items.append(item)

    context["seo_breadcrumbs"] = trail
    context["seo_breadcrumb_json"] = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": items,
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )
    return context
