import time
from pynput.keyboard import Key, Controller

x = "put spam here"
list_x = x.split()


keyboard = Controller()

#10 seconds to switch
time.sleep(10)


i=0;

#set i to # of spam words
while i!=100 :
    keyboard.type(x)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    i+=1

print("done2")
