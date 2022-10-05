# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "Developer Portal"

extensions = [
    # Support markdown
    "myst_parser",
    # For the card element
    "sphinx_design",
    # To allow the toc tree to be defined in a single file
    "sphinx_external_toc",
]

# Allow the ::::: syntax we use for grids
myst_enable_extensions = ["colon_fence"]

# Where to find the tox
external_toc_path = "toc.yaml"

# If true, Sphinx will warn about all references where the target cannot
# be found.
nitpicky = True

# The master toctree document.
master_doc = "index"

# Common links that should be available on every page
rst_epilog = """
.. _Diamond Light Source: http://www.diamond.ac.uk
.. _black: https://github.com/psf/black
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _isort: https://github.com/PyCQA/isort
.. _mypy: http://mypy-lang.org/
.. _pre-commit: https://pre-commit.com/
"""

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
github_repo = "developer-portal-ideas"
github_user = "DiamondLightSource"

# Theme options for pydata_sphinx_theme
html_theme_options = dict(
    show_nav_level=2,
    logo=dict(
        text=project,
    ),
    use_edit_page_button=True,
    github_url=f"https://github.com/{github_user}/{github_repo}",
)

# A dictionary of values to pass into the template engine’s context for all pages
html_context = dict(
    github_user=github_user,
    github_repo=project,
    github_version="main",
    doc_path="docs",
)

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# Logo
html_logo = "images/dls-logo.svg"
html_favicon = "images/dls-favicon.ico"
