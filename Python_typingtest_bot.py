import pyautogui
import time


string='YOUR String here'
st=string.split(' ')
s=len(st)# length of words in string
i=0
time.sleep(4)
while(i<s): # Length of string
 pyautogui.typewrite(st[i])
 pyautogui.press('space')
 i=i+1
