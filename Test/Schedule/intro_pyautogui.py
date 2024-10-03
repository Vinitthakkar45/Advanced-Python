# import pyautogui
# screenWidth, screenHeight = pyautogui.size()
# currentMouseX, currentMouseY = pyautogui.position()
# print(screenWidth, screenHeight, currentMouseX, currentMouseY)

# pyautogui.moveTo(1000, 1000,5)

# pyautogui.click()
# pyautogui.rightClick()
# pyautogui.moveTo(screenWidth / 2, screenHeight / 2,3)


# import pyautogui
# import time
# # Open Notepad
# pyautogui.press('win')
# pyautogui.write('Notepad')
# pyautogui.press('enter')
# time.sleep(1)
# # Type a message and save it
# pyautogui.write("Hello, world!")
# pyautogui.hotkey('ctrl', 's')


# import pyautogui
# # Take a screenshot
# screenshot = pyautogui.screenshot()
# # Save the screenshot
# screenshot.save('screenshot.png')
# # Take a screenshot of a specific region (x, y, width, height)
# # region_screenshot = pyautogui.screenshot(region=(0, 0, 300, 400))
# # region_screenshot.save('region_screenshot.png')



# # Locate an image on the screen
# location = pyautogui.locateOnScreen('screenshot.png')

# if location:
#     print(f"Image found at: {location}")
#     # Move the mouse to the center of the located image
#     pyautogui.moveTo(location.left + location.width / 2, location.top + location.height / 2)
#     # Click on the center of the located image
#     pyautogui.click()
# else:
#     print("Image not found!")



# import pyautogui
# import time
# # Open the default web browser (works on Windows)
# pyautogui.hotkey('win', 'r')
# pyautogui.write('chrome')
# pyautogui.press('enter')
# time.sleep(2)
# # Search for 'PyAutoGUI'
# pyautogui.write('PyAutoGUI')
# pyautogui.press('enter')
# time.sleep(8)
# # Take a screenshot of the results
# pyautogui.screenshot('search_results.png')



import pyautogui
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
print(screenWidth, screenHeight) # (2560, 1440)
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
print(currentMouseX, currentMouseY) #(1314, 345)
pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.
pyautogui.click() # Click the mouse.
pyautogui.click(100, 200) # Move the mouse to XY coordinates and click it.
# pyautogui.click('button.png') # Find where button.png appears on the screen and click it.
pyautogui.move(400, 0) # Move the mouse 400 pixels to the right of its current position.
pyautogui.doubleClick() # Double click the mouse.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to 
# Hello world! mouse over 2 Hello world! world! world!.
pyautogui.write('Hello world!', interval=0.25) # type with quarter-second pause in between each key
pyautogui.press('esc') # Press the Esc key. All key names are in pyautogui.KEY_NAMES
with pyautogui.hold('shift'): # Press the Shift key down and hold it.
    pyautogui.press(['down', 'down', 'down', 'down']) # Press the left arrow key 4 times. # Shift key is released 
pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.
# automatically.
# pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.
pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is 