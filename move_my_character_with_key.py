from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

character = load_image('charater.png')
#너비 124, 높이 126

def handle_events():
    global running, x, y, dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir = 6
            elif event.key == SDLK_LEFT:
                dir = 4
            elif event.key == SDLK_UP:
                dir = 8
            elif event.key == SDLK_DOWN:
                dir = 2
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
                dir = 0

def draw_charater():
    global x, y
    if dir == 6:
        character.clip_draw(frame * 124, 126 * 1, 124, 126, x, y)
    elif dir == 8:
        character.clip_draw(frame * 124, 126 * 0, 124, 126, x, y)
    elif dir == 4:
        character.clip_draw(frame * 124, 126 * 2, 124, 126, x, y)
    elif dir == 2:
        character.clip_draw(frame * 124, 126 * 3, 124, 126, x, y)

running = True
frame = 0
x, y = TUK_WIDTH // 2 , TUK_HEIGHT // 2
dir = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    draw_charater()
    update_canvas()
    handle_events()
    frame = (frame + 1) % 4
    delay(0.05)

close_canvas()