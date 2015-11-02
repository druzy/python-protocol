from pychromecast import Chromecast
from wait_init import wait_init
import sys

cast=Chromecast(sys.argv[1])
wait_init(cast)
cast.start_app(sys.argv[2])