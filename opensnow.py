# Open snow api reader.  Caches the forcasts for up to 24hrs to reduce API requests

from google.appengine.api import urlfetch
from urllib import urlencode

class OpenSnow(object):
    API_KEY = "1c969c1b39ee6293"
    API_URL = "http://api.wunderground.com/api/%s/forecast10day/q/CA/Squaw_Valley.json" % API_URL
    
    

    url = 