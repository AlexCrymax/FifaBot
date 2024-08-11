import pyautogui
import time


for i in range(50):
    
    pick = pyautogui.locateCenterOnScreen("pick.png", confidence= 0.5)

    pyautogui.moveTo(pick, duration = 0.1)
    pyautogui.leftClick()

    time.sleep(1.5)
    
    build = pyautogui.locateCenterOnScreen("build.png", confidence= 0.5)

    pyautogui.moveTo(build, duration = 0.1)
    pyautogui.leftClick()

    time.sleep(3)

    submit = pyautogui.locateCenterOnScreen("submit.png", confidence = 0.5)

    pyautogui.moveTo(submit, duration = 0.1)
    pyautogui.leftClick()

    time.sleep(1.5)
    
    claim = pyautogui.locateCenterOnScreen("claim.png")

    pyautogui.moveTo(claim, duration = 0.1)
    pyautogui.leftClick()

    claim = pyautogui.locateCenterOnScreen("claim.png")

    pyautogui.moveTo(claim, duration = 0.1)
    pyautogui.leftClick()
    
    print(f"{i+1} out of 50")
    
    time.sleep(2)
    
    #babysitter
    
    if (i + 1) % 10 == 0:
        print("babysitter on, sleeping for 50 seconds")
        time.sleep(50)
        

        