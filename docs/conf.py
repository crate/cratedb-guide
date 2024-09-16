from crate.theme.rtd.conf.cratedb_guide import *

# Fallback guards, when parent theme does not introduce them.
if "html_theme_options" not in globals():
    html_theme_options = {}
if "intersphinx_mapping" not in globals():
    intersphinx_mapping = {}

# Re-configure sitemap generation URLs.
# This is a project without versioning.
sitemap_url_scheme = "{link}"

# Disable version chooser.
html_context.update({
    "display_version": False,
    "current_version": None,
    "versions": [],
})

# Configure link checker.
linkcheck_ignore = [
    # Generic ignores.
    r"http://localhost:\d+/",
    # Forbidden by WordPress.
    r"https://cratedb.com/wp-content/uploads/2018/11/copy_from_population_data.zip",
    # Forbidden by Stack Overflow.
    r"https://stackoverflow.com/.*",
    # Expired certificate.
    r"https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/index.html",
    # 403 Client Error: Forbidden for url
    r"https://www.baeldung.com/.*",
    # 404 Client Error: Not Found
    r"https://github.com/crate-workbench/cratedb-toolkit/actions/runs/.*",
    # 403 Client Error: Forbidden for url
    r"https://www.datacamp.com/.*",
    # Read timed out. (read timeout=15)
    r"https://www.imf.org/.*",
    # -rate limited-, sleeping...
    r"https://medium.com/.*",
    r"http://api.open-notify.org/.*",
]

# Configure intersphinx.
if "sphinx.ext.intersphinx" not in extensions:
    extensions += ["sphinx.ext.intersphinx"]

if "intersphinx_mapping" not in globals():
    intersphinx_mapping = {}

intersphinx_mapping.update({
    'ctk': ('https://cratedb-toolkit.readthedocs.io/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    })


# Configure substitutions.
if "myst_substitutions" not in globals():
    myst_substitutions = {}

myst_substitutions.update({
    "nb_colab": "[![Notebook on Colab](https://img.shields.io/badge/Open-Notebook%20on%20Colab-blue?logo=Google%20Colab)]",
    "nb_binder": "[![Notebook on Binder](https://img.shields.io/badge/Open-Notebook%20on%20Binder-lightblue?logo=binder)]",
    "nb_github": "[![Notebook on GitHub](https://img.shields.io/badge/Open-Notebook%20on%20GitHub-darkgreen?logo=GitHub)]",
    "readme_github": "[![README](https://img.shields.io/badge/Open-README-darkblue?logo=GitHub)]",
    "blog": "[![Blog](https://img.shields.io/badge/Open-Blog-darkblue?logo=Markdown)]",
    "tutorial": "[![Navigate to Tutorial](https://img.shields.io/badge/Navigate%20to-Tutorial-darkcyan?logo=Markdown)]",
    "readmore": "[![Read More](https://img.shields.io/badge/Read-More-darkyellow?logo=Markdown)]",
})
