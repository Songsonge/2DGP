from pico2d import *

def handle_events():
    global running
    global x,y
    global to_x, to_y
    global move
    global movedirection
    global i
    global mouse_x,mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_MOUSEBUTTONDOWN:
            to_x, to_y = event.x, get_canvas_height() - 1 - event.y
            if to_x > x:
                movedirection = 1
            else:
                movedirection = 0
            i=0
            move = True
        if event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, get_canvas_height() - 1 - event.y
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False




open_canvas()
gra = load_image('grass.png')
cha = load_image('run_animation.png')

running = True
x = 0
y = 0
frame = 0
move = False

while running:
    if move:
        while x < 800:
            clear_canvas()
            gra.draw(400,30)
            t = i / 1000
            x = (1 - t) * x + t * to_x
            cha.clip_draw(frame*100,0,100,100,x,85)
            update_canvas()
            frame = (frame + 1) % 8
            handle_events()
            i += 1

            delay(0.05)
        move = False
    else:
        clear_canvas()
        gra.draw(400,30)
        cha.clip_draw(frame*100,0,100,100,x,85)
        update_canvas()
        frame = (frame + 1) % 8

        delay(0.05)
    handle_events()

close_canvas()
