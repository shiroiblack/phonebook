from pathlib import Path


path = Path()
sa = path.glob('*.*')
for files in sa:
    print(files)