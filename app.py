from pathlib import Path


path = Path()
for file in path.glob('*.py'):
    print(file)

path_1 = Path("Test")
print(path_1.exists())

path_new = Path("emails")
print(path_new.mkdir())
print(path_new.rmdir())
