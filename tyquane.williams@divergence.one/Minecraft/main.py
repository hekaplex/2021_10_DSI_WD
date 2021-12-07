from ursina import *

class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45, 45, 45)
            )

class Test_button(Button):
    def __init__(self):
        super().__init__(    
            parent = scene,
            model = 'cube',
            texture = 'brick',
            color = color.blue)


def update():
    if held_keys['a']:
        test_square.x -= 4 * time.dt


app = Ursina()

test_square = Entity(model = 'quad', color = color.red, scale = (1, 4), position = (5,4))

sans_texture = load_texture('Assets/Minecraft/Sans.png')
sans = Entity(model = 'quad', texture = sans_texture)

test_cube = Test_button()

app.run()

