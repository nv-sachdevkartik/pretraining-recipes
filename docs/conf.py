"""Sphinx configuration for Pretraining Recipes."""

from __future__ import annotations

project = "Pretraining Recipes"
author = "Kartik Sachdev"
copyright = "2026, Kartik Sachdev"
release = "0.1"
version = "0.1"

extensions = [
    "myst_parser",
    "sphinx.ext.githubpages",
    "sphinx_copybutton",
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
html_title = "Pretraining Recipes"
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
    "show_toc_level": 2,
    "collapse_navigation": True,
    "use_sidenotes": True,
    "logo": {
        "text": "Pretraining Recipes",
    },
}
