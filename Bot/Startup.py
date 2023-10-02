import time
import subprocess

def initialize():
    print("Initializing the application...")
    time.sleep(5)



if __name__ == "__main__":
    initialize()
    
    print("Running the main application.")
    time.sleep(2)
    
    subprocess.run(["python", "Source-Code/main.py"])
