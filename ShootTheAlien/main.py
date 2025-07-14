import pgzrun
import random

WIDTH = 500
HEIGHT = 500

alien = Actor("alien")
alien.pos = 100, 100

def draw():
    screen.clear()
    alien.draw()

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        alien.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

pgzrun.go()
