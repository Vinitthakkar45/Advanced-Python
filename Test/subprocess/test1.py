import subprocess
import sys
try:
    result = subprocess.run([sys.executable, "-c", "import time; time.sleep(3);print(1)"],timeout=2)

# result=subprocess.run(['python',"-c", "print('Hello')"], shell=True, capture_output=True, timeout=6)
except:
    print("Timeout")
