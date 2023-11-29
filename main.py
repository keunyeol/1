결과 = 0

def on_button_pressed_a():
    music.play(music.builtin_playable_sound_effect(soundExpression.twinkle),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global 결과
    결과 = randint(1, 3)
    if 결과 == 1:
        basic.show_icon(IconNames.SCISSORS)
    elif 결과 == 2:
        basic.show_icon(IconNames.CHESSBOARD)
    else:
        basic.show_icon(IconNames.PITCHFORK)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    music.play(music.builtin_playable_sound_effect(soundExpression.sad),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)
