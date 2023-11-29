Libraries required:
 - mss
 - numpy
 - cv2 (OpenCV)
 - pyautogui
 - "Helpers" folder must also be available

ReactionTime.py starts by waiting for the "Reaction Time Test" screen to appear on primary (or targeted)
monitor. It will then start taking screenshots using mss for fastest reaction times possible. It will
wait for screen to be the specified red color and then click upon changing to the specified green color.

**Note: Width and Height must be changed to targeted monitor resolution. Red and Green RGB values
might also need to be changed based on machine.**

