import time

def wait_init(cast):
    while (cast.status==None):
        time.sleep(1)
        
    while (cast.media_controller.status==None):
        time.sleep(1)
    
    time.sleep(1)
    return