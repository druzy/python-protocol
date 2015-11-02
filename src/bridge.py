from pychromecast import Chromecast
from wait_init import wait_init
import sys

cast=Chromecast(sys.argv[1])
wait_init(cast)

ask=raw_input()

while ask!="exit":
    
    if ask=="play":
        cast.media_controller.play()
    
    if ask=="pause":
        cast.media_controller.pause()
        
    if ask=="stop":
        cast.media_controller.stop()

    if ask=="seek":
        seek=raw_input()
        cast.media_controller.seek(int(seek))
        cast.media_controller.update_status()

    if ask=="volume":
        volume=float(raw_input())
        cast.set_volume(volume)
        cast.media_controller.update_status()
        
    if ask=="launch_app":
        app_id=raw_input()
        cast.start_app(app_id)
        
    if ask=="quit_app":
        cast.quit_app();
        
    if ask=="send":
        url=raw_input()
        mimetype=raw_input()
        cast.play_media(url,mimetype)
        
    if ask=="media_status":
        cast.media_controller.update_status()
        status=cast.media_controller.status
        print(6)
        print("ask="+ask)
        if (status.current_time==None):
            print("current_time=0") 
        else:
            print("current_time="+str(status.current_time))
        if (status.duration==None):
            print("duration=0")
        else:
            print("duration="+str(status.duration))
        print("volume_level="+str(status.volume_level))
        print("volume_muted="+str(status.volume_muted))
        print("player_state="+status.player_state)
        
    ask=raw_input()