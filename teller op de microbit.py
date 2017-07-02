from microbit import *
teller = 0

while True:
    if pin5.read_digital():
        teller+1

    if pin11.read_digital():
        teller = 0
    display.show(teller)
 