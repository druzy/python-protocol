from __future__ import print_function
from pychromecast import Chromecast
import sys

cast=Chromecast(sys.argv[1])
cast.media_controller.play_media(sys.argv[2],sys.argv[3],autoplay=False)