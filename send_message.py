import time
import pywhatkit    # py -m pip install pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller   # py -m pip install pynput

keyboard = Controller()

def send_whatsapp_message(msg:str):
    try:#طريقة بهندل بيها exceptions  بشكل مودرن

#pywhatkit.sendwhatmsg_instantly(
            #phone_no= "+0201145070573" ,
        # message=msg ,
    #tab_close = True 
        #) #send to phone no.


        pywhatkit.sendwhatmsg_to_group_instantly("CJRjyJBgX2F7Yx2mGYor3r",
        message=msg ,
        tab_close = True 
        ) #send to group 
        
        time.sleep(5)
        pyautogui.click()
        time.sleep(3)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("message sent")
    except Exception as e:
        print(str(e))

if __name__ == "__main__" :
    send_whatsapp_message(msg="hello from automated message :) #nour ")  # syntax: group id, message, hour and minutes
#pywhatkit.sendwhatmsg_to_group("write-id-here", "Message 3", 19, 2)



    # python .\send_message.py to run file from terminal 