"""Sphinx configuration for Pretraining Recipes."""

from __future__ import annotations

project = "Pretraining Recipes"
author = "Kartik Sachdev"
copyright = "2026, Kartik Sachdev"
release = "0.1"
version = "0.1"
root_doc = "index"

extensions = [
    "myst_parser",
    "sphinx.ext.githubpages",
    "sphinx_copybutton",
    "sphinx_design",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "README.md",
    "index.md",
    "index.html",
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "substitution",
    "tasklist",
]

html_theme = "sphinx_book_theme"
html_title = "VLA Training Recipes Documentation"
html_show_sphinx = False
html_last_updated_fmt = ""
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]

html_theme_options = {
    "repository_url": "https://github.com/nv-sachdevkartik/pretraining-recipes",
    "path_to_docs": "docs",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "show_toc_level": 1,
    "collapse_navigation": True,
    "use_sidenotes": True,
    "logo": {
        "text": "VLA Training Recipes",
    },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/nv-sachdevkartik/pretraining-recipes",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
        {
            "name": "Public Docs",
            "url": "https://nv-sachdevkartik.github.io/pretraining-recipes/",
            "icon": "fa-solid fa-book-open",
            "type": "fontawesome",
        },
    ],
    "icon_links_label": "Project links",
}

html_sidebars = {
    "**": [
        "navbar-logo.html",
        "icon-links.html",
        "search-field.html",
        "sbt-sidebar-nav.html",
    ]
}
