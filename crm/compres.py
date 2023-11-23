from .settings import STATIC_URL
# COMPRESS_ROOT = BASE_DIR + "/static/"
COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.CSSMinFilter",
]

COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"]
COMPRESS_FILTERS = {
    "css": [
        "compressor.filters.css_default.CssAbsoluteFilter",
        "compressor.filters.cssmin.rCSSMinFilter",
    ],
}
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
# COMPRESS_COMPILERS = (
#     'text/x-scss', 'django_libsass.SassCompiler',
# )
COMPRESS_OFFLINE_CONTEXT = {
    "STATIC_URL": "STATIC_URL",
}

COMPRESS_REBUILD_TIMEOUT = 5400


COMPRESS_OUTPUT_DIR = "CACHE"
COMPRESS_URL = STATIC_URL

COMPRESS_PRECOMPILERS = (
    ("text/less", "lessc {infile} {outfile}"),
    ("text/x-sass", "sass {infile} {outfile}"),
    ("text/x-scss", "sass {infile} {outfile}"),
)

COMPRESS_OFFLINE_CONTEXT = {
    "STATIC_URL": "STATIC_URL",
}
