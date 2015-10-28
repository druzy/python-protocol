from __future__ import print_function
import pychromecast

casts=pychromecast.get_chromecasts_as_dict()
for key in casts.keys():
    cast=casts.get(key)
    print("2")
    print("ip="+cast.host)
    print("name="+cast.device.friendly_name)
    