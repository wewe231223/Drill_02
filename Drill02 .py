from pico2d import *
import  math

open_canvas(800,600)
clear_canvas_now()

ch = load_image("character.png")
gr = load_image("grass.png")





cx = 400
cy = 90

Width = get_canvas_width() - 30
Height = get_canvas_height() - 30


print(Width)
print(Height)
SqareMovement = True
CircleMovement = False

def Sqare(char : Image,grass : Image):
    x = 400
    y = 90

    while x < Width :
        clear_canvas_now()
        x += 3
        char.draw_now(x,y)
        grass.draw_now(400,30)

    while y < Height:
        clear_canvas_now()
        y += 3
        char.draw_now(x,y)
        grass.draw_now(400, 30)

    while x > 0 :
        clear_canvas_now()
        x -= 3
        char.draw_now(x,y)
        grass.draw_now(400, 30)

    while y > 90:
        clear_canvas_now()
        y -= 3
        char.draw_now(x,y)
        grass.draw_now(400, 30)

    while x < 400:
        clear_canvas_now()
        x += 3
        char.draw_now(x,y)
        grass.draw_now(400, 30)


def Circle(char : Image , grass : Image):
    t = 0
    x = 400
    y = 90
    while t < 360:
        clear_canvas_now()
        x = x +  4 * math.cos(math.pi * (t / 180))
        y = y +  4 * math.sin(math.pi * (t /180))
        char.draw_now(x,y)
        grass.draw_now(400,30)

        t += 1
        delay(0.01)



while True:
    Sqare(ch,gr)
    Circle(ch,gr)

    get_events()
close_canvas()