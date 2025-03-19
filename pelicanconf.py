AUTHOR = 'SystemError'
SITENAME = 'SystemError Collective'

PATH = "src/content"
THEME = "src/theme"
OUTPUT_PATH  = ".out/"

TIMEZONE = 'Europe/Stockholm'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    # ("Pelican", "https://getpelican.com/"),
    # ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    # ("Instagram", "https://www.instagram.com/system.error_collective/"),
    # ("Soundcloud", "https://soundcloud.com/systemerrorcollective"),
    # ("Youtube", "https://www.youtube.com/@systemerrorcollective"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Whether to display pages on the menu of the template. Templates may or may not honor this setting.
DISPLAY_PAGES_ON_MENU = True

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

DELETE_OUTPUT_DIRECTORY = True

# Needed so that github pages can find the stylesheets
RELATIVE_URLS = True