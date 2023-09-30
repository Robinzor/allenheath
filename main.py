import subprocess
import pyautogui
import time

# Simulate pressing the Super (Windows) key twice quickly
pyautogui.hotkey('winleft')
time.sleep(0.1)
pyautogui.hotkey('winleft')
time.sleep(0.1)

# Start the Java application and get its process ID (PID)
process = subprocess.Popen("java -jar ~/App/DL5000SystemManager.jar", shell=True)
pid = process.pid

# Wait for a moment to allow the window to appear
time.sleep(5)

# Use wmctrl to find the window by title
result = subprocess.run("wmctrl -lx | grep 'DL5000'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
window_info = result.stdout.decode().strip().split(' ')

if len(window_info) >= 1:
    window_id = window_info[0]
    # Maximize the window by its ID
    subprocess.run(f"wmctrl -i -r {window_id} -b add,maximized_vert,maximized_horz", shell=True)
    # Set the window to fullscreen mode
    subprocess.run(f"wmctrl -i -r {window_id} -b toggle,fullscreen", shell=True)
else:
    print("Window not found.")
