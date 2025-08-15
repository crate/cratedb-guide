from crate.theme.rtd.conf.cratedb_guide import *

# Fallback guards, when parent theme does not introduce relevant variables.
if "html_css_files" not in globals():
    html_css_files = []
if "html_theme_options" not in globals():
    html_theme_options = {}
if "intersphinx_mapping" not in globals():
    intersphinx_mapping = {}
if "linkcheck_ignore" not in globals():
    linkcheck_ignore = []
if "linkcheck_anchors_ignore_for_url" not in globals():
    linkcheck_anchors_ignore_for_url = []

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
linkcheck_ignore += [
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
    # Read timed out. (read timeout=15)
    r"https://azure.microsoft.com/.*",
    # 403 Client Error: Forbidden for url
    r"https://www.mysql.com/.*",
    r"https://dev.mysql.com/.*",
    # HTTPSConnectionPool(host='www.softwareag.com', port=443): SSL: CERTIFICATE_VERIFY_FAILED
    r"https://www.softwareag.com/.*",
    # 403 Client Error: Forbidden for url
    r"https://dzone.com/.*",
    # 504 Client Error: Gateway Timeout for url
    r"https://web.archive.org/.*",
    # 403 Client Error: Forbidden for url
    r"https://www.tableau.com/",
    # Read timed out. (read timeout=15)
    r"https://kubernetes.io/",
    # Connection to renenyffenegger.ch timed out.
    r"https://renenyffenegger.ch",
    # Failed to establish a new connection: [Errno 111] Connection refused
    r"https://www.amqp.org/",
    # "We are currently migrating Datatracker and Mail Archive to a new cloud provider."
    r"https://datatracker.ietf.org",
    # 403 Client Error: Forbidden
    r"https://www.sqlalchemy.org/",
]

linkcheck_anchors_ignore_for_url += [
    # Anchor 'XXX' not found
    r"https://pypi.org/.*"
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


html_css_files += [
    'css/custom.css',
]
