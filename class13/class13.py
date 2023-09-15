from microbit import *

while True:
    if button_a.is_pressed():
        music.play('C4:4')  # DO
        music.play('D4:4')  # RE
        music.play('E4:4')  # ME

    if button_b.is_pressed():
        music.stop()