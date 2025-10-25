from pathlib import Path
current=Path(".")
for item in current.iterdir():
    print(item)
    if item.is_file():
        print(f"  - This is a file: {item.name}")
    elif item.is_dir():
        print(f"  - This is a directory: {item.name}")