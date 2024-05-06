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
]

# Configure intersphinx.
intersphinx_mapping.update({
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    })
