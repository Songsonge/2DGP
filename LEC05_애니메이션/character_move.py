from pico2d import *

open_canvas()

gra=load_image('grass.png')
ch=load_image('run_animation.png')



x=0
frame_index=0
while x<800:
    clear_canvas()
    gra.draw(400,30)
    ch.clip_draw(100*frame_index,0,100,100,x,85)
    update_canvas()

    get_events()
    
    x+=2
   # frame_index+=1
    #if frame_index>=800:frame_index=0
    frame_index=(frame_index+1)%8
    
    delay(0.02)

delay(1)

close_canvas()
    
