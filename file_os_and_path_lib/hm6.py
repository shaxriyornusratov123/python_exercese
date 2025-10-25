import os
try:
    os.makedirs("home/shaxriyor/Projects/python_exercese/file_hm/hm9.py")
except FileExistsError:
    print("bu file oldin yaratilgan")