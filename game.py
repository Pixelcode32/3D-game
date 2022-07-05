from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.audio import Audio

app = Ursina()
window.exit_button.enabled = False

window.fullscreen = False
#player
player = FirstPersonController(
    Collider = 'box'
)


player.speed = 8
player.jump_height = 2.5


#world options
a = Audio('2019-06-07_-_Chill_Gaming_-_David_Fesliyan.mp3', pitch=1, loop=True, autoplay=True, volume = 2)
Sky(texture="sky_sunset")



box = Entity(
    model='cube',
    texture="white_cube",
    collider='box',
    color = color.cyan,
    scale=(2, 0.5, 2),
)

app.run()
