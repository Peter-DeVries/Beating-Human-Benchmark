Libraries required:
 - mss
 - numpy
 - cv2 (OpenCV)
 - pyautogui
 - "Helpers" folder must also be available

AimTrainer.py starts by waiting for the "Aim Trainer" screen to appear on primary (or targeted)
monitor. It will then start taking screenshots using mss for fastest reaction times possible. It will then
click on all targets and stop once the "Save Score" button appears. It recognizes the targets by their
light blue color and the stop button by its yellow color.

**Note: Width and Height must be changed to targeted monitor resolution. Target and Stop RGB values
might also need to be changed based on machine.**

