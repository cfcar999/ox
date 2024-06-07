x = 0

def on_button_pressed_a():
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_screen_up():
    global x
    x = randint(1, 6)
    if x == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        music.play(music.create_sound_expression(WaveShape.SINE,
                3853,
                0,
                183,
                0,
                2000,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LOGARITHMIC),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(200)
        basic.clear_screen()
        basic.pause(200)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        basic.pause(200)
        basic.clear_screen()
        basic.pause(200)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        basic.pause(200)
    elif x == 2:
        basic.show_leds("""
            . . . . .
            . . . # .
            . . . . .
            . # . . .
            . . . . .
            """)
    elif x == 3:
        basic.show_leds("""
            . . . . .
            . . . # .
            . . # . .
            . # . . .
            . . . . .
            """)
    elif x == 4:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            """)
    elif x == 5:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . # . .
            . # . # .
            . . . . .
            """)
    else:
        basic.show_leds("""
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            """)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)
