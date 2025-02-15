import time 
import keyboard
def clock():
    t = time.strftime("%H:%M:%S")
    print(
        f"time = {t}\r",
        end=""
        )

while True:
    clock()
    time.sleep(1)
    if keyboard.is_pressed('e'):
        print("You pressed 'e'. Exiting...") 
        break 
