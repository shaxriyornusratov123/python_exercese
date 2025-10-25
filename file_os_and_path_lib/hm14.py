import os 
from pathlib import Path
import glob
os.chdir("file_os_and_path_lib")
current=Path(".")
for file in current.glob("*.py"):
    print(file)