import random, pyautogui as pyauto

for x in range(10):
    height = random.randint(0, 1080)
    width = random.randint(0, 1920)
    pyauto.click(height, width, duration=0.3)
    pyauto.hotkey('winleft', 'm')
