import os
import shutil

path = os.path.dirname(os.path.abspath(__file__))

for folder in ["A_NAMES", "B_NAMES"]:
    os.makedirs(os.path.join(path, folder), exist_ok=True)

for file in os.listdir(path):
    full_path = os.path.join(path, file)

    if not os.path.isfile(full_path):
        continue

    if file.lower().endswith(".txt"):
        if file.lower().startswith("a"):
            shutil.copy2(full_path, os.path.join(path, "A_NAMES", file))
        elif file.lower().startswith("b"):
            shutil.copy2(full_path, os.path.join(path, "B_NAMES", file))