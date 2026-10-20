"""Build visible breadcrumbs and matching JSON-LD from the MkDocs navigation."""

import json


ROOT_LABEL = "خانه"


def on_page_context(context, page, config, **kwargs):
    """Expose a single breadcrumb model to both HTML and JSON-LD templates."""
    if page.url in ("", "index.html"):
        context["seo_breadcrumbs"] = []
        context["seo_breadcrumb_json"] = ""
        return context

    site_url = config.site_url
    # GitHub Pages serves this project under /silk-road/, so the domain root
    # is not the book's homepage. Use the configured canonical site URL.
    trail = [{"name": ROOT_LABEL, "url": site_url}]
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
