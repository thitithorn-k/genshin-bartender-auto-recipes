import win32gui
import time
from PIL import ImageGrab
import cv2
import numpy as np


def get_screen(test=False):
    try:
        toplist, winlist = [], []

        def enum_cb(hwnd, results):
            winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

        win32gui.EnumWindows(enum_cb, toplist)

        genshin = [(hwnd, title) for hwnd, title in winlist if ('genshin impact' or '原神') in title.lower() and len(title) < 15]
        if test:
            if genshin:
                return True
            else:
                return False
        if not genshin:
            print('genshin\'s window not found')
            return -1

        hwnd = genshin[0]

        win32gui.SetForegroundWindow(hwnd[0])
        time.sleep(.05)
        bbox = win32gui.GetWindowRect(hwnd[0])
        screen_img = ImageGrab.grab(bbox)

        screen_img = np.array(screen_img)
        screen_img = cv2.cvtColor(screen_img, cv2.COLOR_BGR2RGB)
        return screen_img
    except:
        return -1