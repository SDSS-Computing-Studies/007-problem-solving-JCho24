import time as t
import pyautogui as p


def button():
    # Locate the off button and move to it

    offlist = p.locateCenterOnScreen("ButtonOff.png")
    offmove = p.moveTo(x = offlist[0], y = offlist[1], duration = 0.2)
    print("Moved to the button!")

        # Now we start clicking on the On button
    
    while 2>1:
        onbuttonclick = p.click(x=offlist[0], y=offlist[1], clicks=10, interval=0.13, button='left')
        print("CLICKING BUTTON!!!")

    return onbuttonclick

button()