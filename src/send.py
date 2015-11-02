from pychromecast import Chromecast
from wait_init import wait_init
import sys

cast=Chromecast(sys.argv[1])
wait_init(cast)
cast.media_controller.play_media(sys.argv[2],sys.argv[3])