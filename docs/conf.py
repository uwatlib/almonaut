# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
from typing import Any, Dict

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)

# -- Project information -----------------------------------------------------

project = 'Almonaut'
copyright = '2022, University of Waterloo'
author = 'University of Waterloo'
version = '0.1'
release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages',
    'sphinx_autodoc_typehints',
    'sphinx_copybutton'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# sphinx.ext.autodoc options
autodoc_member_order = 'bysource'

# sphinx_autodoc_typehints
always_document_param_types = True
typehints_defaults = 'comma'

# -- Options for HTML output -------------------------------------------------

#html_theme = 'sphinx_rtd_theme'
html_theme = 'furo'
html_static_path = ['_static']
html_logo = 'almonaut_logo_250x194.png'
html_css_files = ['css/custom.css']

html_theme_options: Dict[str, Any] = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/uwatlib/almonaut",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
    #"source_repository": "https://github.com/uwatlib/almonaut/",
    #"source_branch": "main",
    #"source_directory": "docs/",
}


# sphinx_rtd_theme options
#html_theme_options = {
    #'navigation_depth': 3,
#}

# furo theme options
html_title = f"{project} v{version}"
