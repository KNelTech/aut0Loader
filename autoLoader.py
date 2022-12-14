# Import the necessary modules
import time
import pyautogui

# Set the file path for the data to be copied
file_path = "C:/Users/17738/Desktop/data_file.txt"

# Open the file and read the data line by line
with open(file_path, "r") as f:
    lines = f.readlines()


# Set the interval between clicks (in seconds)
click_interval = 2

# Wait for 10 seconds before starting the script
time.sleep(5)

# Continuously click the mouse and paste each line of data
for line in lines:
    # Click the mouse at the current position
    pyautogui.click()

    # Paste the data
    pyautogui.typewrite(line)

    # Wait for the specified interval
    time.sleep(click_interval)



