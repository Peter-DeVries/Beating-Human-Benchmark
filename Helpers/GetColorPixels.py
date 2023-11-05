from ScreenGrabber import *

# Windows
width = 2560
height = 1440

# Mac
# width = 1440
# height = 900


x, y = 760, 432

screen_grabber = ScreenGrabber(0, 0, width, height, -1)
screen_grabber.take_screen_shot()


def get_color_pixels():
    print(screen_grabber.get_pixel_color(x, y))


if __name__ == '__main__':
    get_color_pixels()
