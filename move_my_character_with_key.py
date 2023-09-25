from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

character = load_image('charater.png')

def handle_events():
    global running, x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
frame = 0
x, y = TUK_WIDTH // 2 , TUK_HEIGHT // 2


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    #캐릭터 그리기
    update_canvas()
    handle_events()
    frame = (frame + 1) % 4
    delay(0.05)

close_canvas()