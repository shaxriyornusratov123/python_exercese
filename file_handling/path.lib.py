# Write “Hello, World!” to temp_data/greeting.txt using Path.write_text().
from pathlib import Path 
Path.write_text(Path("./hi.txt"),"hello")