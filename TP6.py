humidité = 0

def on_button_pressed_a():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(input.light_level())
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    if humidité < 60:
        basic.show_string("Veiller arroser la plante")
    else:
        basic.show_string("Vous n'avez pas besoin s'arroser la plante")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    if input.light_level() < 120:
        basic.show_string("Les plantes ont besoin de beaucoup plus de lumiere")
    if input.temperature() < 10:
        basic.show_string("Veiller placer les plantes dans un environnement plus chaud")
basic.forever(on_forever)

def on_every_interval():
    global humidité
    humidité = randint(0, 100)
    basic.show_string("H :")
    basic.show_number(humidité)
    if humidité < 60:
        basic.show_string("Veiller appuyer sur le logo pour arroser plante")
loops.every_interval(120000, on_every_interval)
