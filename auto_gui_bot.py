"""
DesktopOrchestrator Pro: High-Fidelity RPA Engine
-------------------------------------------------
An industrial-grade desktop automation suite designed to interface 
with legacy Windows applications via simulated peripheral inputs.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Robotic Process Automation (RPA)
Date: February 2026
"""

import pyautogui
import time
import logging
import subprocess
from pathlib import Path
from typing import Final

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

# 2. Global Safety Configuration
pyautogui.FAILSAFE = True  # Move mouse to TOP-LEFT to abort
pyautogui.PAUSE = 0.5      # Strategic pause between every GUI action

class DesktopOrchestrator:
    def __init__(self):
        self.workspace: Final[Path] = Path.home() / "Documents" / "RPA_Output"
        self._initialize_environment()

    def _initialize_environment(self):
        """Ensures the persistence layer is provisioned."""
        if not self.workspace.exists():
            self.workspace.mkdir(parents=True)
            logging.info(f"Initialized RPA workspace: {self.workspace}")

    def _type_humanized(self, text: str, interval: float = 0.08):
        """Simulates human-like keystroke cadence for anti-detection."""
        pyautogui.write(text, interval=interval)

    def execute_notepad_synthesis(self, filename: str, payload: str):
        """
        Orchestrates the full lifecycle of document creation in Notepad.
        
        :param filename: Target identifier for the asset.
        :param payload: The data string to be injected.
        """
        try:
            logging.info("🚀 Initiating synthesis sequence...")
            
            # Phase 1: Resource Provisioning (Launching Application)
            logging.info("Accessing legacy text editor: Notepad.exe")
            subprocess.Popen(["notepad.exe"])
            time.sleep(1.5)  # Wait for window handle to stabilize

            # Phase 2: Data Injection
            logging.info("Injecting humanized text payload...")
            self._type_humanized(payload)

            # Phase 3: Fiscal Persistence (Saving the file)
            logging.info(f"Executing persistence protocol: {filename}")
            pyautogui.hotkey('ctrl', 's')
            time.sleep(1.0)
            
            # Injection of filename into the Save Dialog
            self._type_humanized(filename)
            pyautogui.press('enter')
            
            # Handling potential overwrite prompts
            time.sleep(0.5)
            logging.info("✅ Document synthesis complete.")

        except pyautogui.FailSafeException:
            logging.critical("🛑 EMERGENCY ABORT: Sentinel Fail-Safe triggered by user.")
        except Exception as e:
            logging.error(f"❌ System Fault: {e}")

if __name__ == "__main__":
    # Standard Operating Procedure (SOP)
    orchestrator = DesktopOrchestrator()
    
    # Define the Professional Payload
    MESSAGE_BODY = (
        "SYSTEM STATUS: ACTIVE\n"
        "-----------------------------------\n"
        "Yang-Tech-Lab Automation Protocol\n"
        "Deliverable: RPA Demonstration\n"
        "Complexity Level: Medium-High\n\n"
        "This node can automate cross-application workflows,\n"
        "bridging hardware logs and executive reporting.\n"
        "-----------------------------------\n"
        "End of Transmission."
    )

    print("--- Desktop Sentinel Offline: System Initializing ---")
    orchestrator.execute_notepad_synthesis(
        filename="Yang_Lab_Report.txt",
        payload=MESSAGE_BODY
    )
    print("--- Session Terminated ---")
