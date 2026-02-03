import pyautogui
import time
import os

print("🚀 Desktop automation bot starting...")
print("⚠️ WARNING: Do not touch your mouse or keyboard while the script is running!")
print("👉 Fail-safe: Move your mouse quickly to the TOP-LEFT corner to abort.")

# 1. Launch Notepad
# Using system command to open the application
print("Opening Notepad...")
os.system("start notepad")
time.sleep(2)  # Wait for the application to initialize

try:
    # 2. Automated typing
    # interval=0.1 adds a 0.1s delay between characters to simulate human typing speed
    print("🤖 Typing message...")
    
    message = "Hello Fiverr Client!\n"
    message += "This message was typed by my Python Bot.\n"
    message += "I can automate ANY desktop application for you.\n"
    message += "Let's save 100 hours of your life!\n\n"
    message += "- Best, Yang"
    
    pyautogui.write(message, interval=0.1)
    
    # 3. Simulate save shortcut (Ctrl + S)
    print("💾 Saving file...")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    
    # 4. Enter filename
    # Interaction with the Save As dialog
    pyautogui.write("robot_note.txt")
    time.sleep(1)
    
    # 5. Press Enter to confirm
    pyautogui.press('enter')
    
    print("🎉 Task complete! File saved successfully.")

except pyautogui.FailSafeException:
    print("🛑 Emergency stop! Fail-safe mechanism triggered by user.")

except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
