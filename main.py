import webbrowser
import pyautogui as pg
import time

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		numbers.append(line.strip())
f.close()
for num in numbers:
    webbrowser.open(f'https://web.whatsapp.com/send?phone={num}&text=Hey!')
    time.sleep(8)
    pg.press('enter')
    time.sleep(5)
    pg.hotkey('ctrl', 'w')