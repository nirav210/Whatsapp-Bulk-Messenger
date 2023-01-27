import webbrowser
import pyautogui as pg
import time
from urllib.parse import quote

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		numbers.append(line.strip())
f.close()

f = open("message.txt", "r")
message = quote(f.read())
f.close()

for num in numbers:
    webbrowser.open(f'https://web.whatsapp.com/send?phone={num}&text={message}')
    time.sleep(8)
    pg.press('enter')
    time.sleep(5)
    pg.hotkey('ctrl', 'w')