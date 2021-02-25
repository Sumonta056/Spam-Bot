import pyautogui
import time
print(" Welcome to SPAM BOT !!! ")
name = input("Enter what you wanted to spam : ")
limit = int(input("How many time the sentence will spam : "))
while limit > 0:
    pyautogui.typewrite(name)
    time.sleep(5)
    pyautogui.press('enter')
    limit = limit - 1





