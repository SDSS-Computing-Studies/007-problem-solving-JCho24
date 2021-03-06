import time as t
import pyautogui as p

def button():

    # Locate the off button and move to it

    offlist = p.locateCenterOnScreen("ButtonOff.png", confidence = 0.8)
    
    if offlist != None:
        offmove = p.moveTo(x = offlist[0], y = offlist[1], duration = 0.2)
        print("Moved to the button!")
        for i in range(0,5):
            onbuttonclick = p.click(x=offlist[0], y=offlist[1], clicks=10, interval=0.05, button='left')
    
    else:
        onlist = p.locateCenterOnScreen("ButtonOn.png", confidence = 0.8)
        if onlist != None:
            onmove = p.moveTo(x = onlist[0], y = onlist[1], duration = 0.2)
            print("Moved to the button!")
            
            for i in range(0,5):
                onbuttonclick = p.click(x=onlist[0], y=onlist[1], clicks=10, interval=0.05, button='left')
    

        print('!')
    # Now we start clicking on the On button with a constant loop until
    # we can upgrade
    print("CLICKING BUTTON!!!")
    

def upgrades1():

    up1list = p.locateCenterOnScreen("Upgrade1.png")
    

    if up1list != None:
        up1move = p.moveTo(x = up1list[0], y = up1list[1], duration = 0.2)
        print("Moved to the Upgrades!")

        up1click = p.click(x=up1list[0], y=up1list[1], clicks=5, interval=0.05, button='left')
        print("UPGRADE 1")
    else:
        print("!", end = "")

    
def upgrades2():

    up2list = p.locateCenterOnScreen("Upgrade2.png")
   

    if up2list != None:
    
        up2move = p.moveTo(x = up2list[0], y = up2list[1], duration = 0.2)
        print("Moved to the Upgrades!")

        up2click = p.click(x=up2list[0], y=up2list[1], clicks=5, interval=0.05, button='left')
        print("UPGRADE 2")



def main():
    
    while True:
        
        k = 1
        while k > 0.5:
            upgrades2()
            t.sleep(0.2)

            upgrades1()
            t.sleep(0.2)

            button()

main()

