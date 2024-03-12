from crate.theme.rtd.conf.cratedb_guide import *

# Fallback guards, when parent theme does not introduce them.
if "html_theme_options" not in globals():
    html_theme_options = {}
if "intersphinx_mapping" not in globals():
    intersphinx_mapping = {}

# Configure sitemap generation URLs.
sitemap_url_scheme = "{link}"

# Configure rel="canonical" link URLs.
html_theme_options.update({
        "canonical_url_path": "%s/" % url_path,
})

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
]

# Configure intersphinx.
if "sphinx.ext.intersphinx" not in extensions:
    extensions += ["sphinx.ext.intersphinx"]

if "intersphinx_mapping" not in globals():
    intersphinx_mapping = {}

intersphinx_mapping.update({
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    })


# Configure substitutions.
if "myst_substitutions" not in globals():
    myst_substitutions = {}

myst_substitutions.update({
    "nb_colab": "[![Notebook on Colab](https://img.shields.io/badge/Open-Notebook%20on%20Colab-blue?logo=Google%20Colab)]",
    "nb_github": "[![Notebook on GitHub](https://img.shields.io/badge/Open-Notebook%20on%20GitHub-darkgreen?logo=GitHub)]",
    "readme_github": "[![README](https://img.shields.io/badge/Open-README-darkblue?logo=GitHub)]",
    "tutorial": "[![Navigate to Tutorial](https://img.shields.io/badge/Navigate%20to-Tutorial-darkcyan?logo=Markdown)]",
})
