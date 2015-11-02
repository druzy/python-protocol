from pychromecast import Chromecast
from wait_init import wait_init
import sys

cast=Chromecast(sys.argv[1])
wait_init(cast)
status=cast.media_controller.status
print(4)
print("current_time="+str(status.current_time))
print("duration="+str(status.duration))
print("volume_level="+str(status.volume_level))
print("volume_muted="+str(status.volume_muted))