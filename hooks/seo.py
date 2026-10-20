"""Build visible breadcrumbs and matching JSON-LD from the MkDocs navigation."""

import json


ROOT_LABEL = "خانه"


def _find_page_path(items, target_url, parents=()):
    for item in items:
        if getattr(item, "is_page", False):
            if item.url == target_url:
                return parents
        elif getattr(item, "is_section", False):
            section_index = next(
                (
                    child
                    for child in item.children
                    if getattr(child, "is_page", False)
                    and child.file.src_uri.endswith("/index.md")
                ),
                None,
            )
            if section_index and section_index.url == target_url:
                return parents
            section_crumb = (
                (item.title, section_index.url)
                if section_index
                else (item.title, None)
            )
            found = _find_page_path(
                item.children, target_url, parents + (section_crumb,)
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
    # Keep the full navigation hierarchy. The domain root is the first
    # breadcrumb, followed by this book's homepage and any section landing page.
    trail = [{"name": ROOT_LABEL, "url": "https://soroush-zendedel.github.io"}]
    trail.append({"name": config.site_name, "url": site_url})

    nav = context.get("nav")
    section_path = _find_page_path(nav.items, page.url) if nav else None
    if section_path:
        trail.extend(
            {"name": name, "url": site_url + url}
            for name, url in section_path
            if url
        )

    trail.append({"name": page.title, "url": site_url + page.url})
    items = []
    for position, crumb in enumerate(trail, start=1):
        item = {
            "@type": "ListItem",
            "position": position,
            "name": crumb["name"],
        }
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
