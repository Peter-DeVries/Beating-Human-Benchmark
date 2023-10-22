import numpy as np
import cv2

from mss import mss


# Class for mss to take screenshots. Will need to change monitor_number depending on the amount of monitors used.
class ScreenGrabber:
    def __init__(self, top_left_x, top_left_y_from_top, width, height):
        self.screen_shot = None
        monitor_number = 1

        with mss() as sct:
            mon = sct.monitors[monitor_number]
            self.monitor = {
                "top": mon["top"] + top_left_y_from_top,
                "left": mon["left"] + top_left_x,
                "width": width,
                "height": height,
                "mon": monitor_number
            }

    # Take a screenshot and stores it in an object
    def take_screen_shot(self):
        with mss() as sct:
            sct_img = sct.grab(self.monitor)
            self.screen_shot = np.array(sct_img)

    # This function shows the current screenshot for 5 seconds, useful for debugging
    def show_screen_shot(self):
        cv2.imshow("Hello", self.screen_shot)
        cv2.waitKey(5000)

    # This function returns the current pixel color of the screenshot
    def get_pixel_color(self, x, y):
        colors = self.screen_shot[y, x]
        return [colors[2], colors[1], colors[0]]
