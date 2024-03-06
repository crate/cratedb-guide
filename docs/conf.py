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
intersphinx_mapping.update({
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    })
