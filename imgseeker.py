from os import listdir
from os.path import isfile, join

extensions = (".jpg", ".png")
only_files = [f for f in listdir(".") if isfile(join("..", f))]
pictures = [p for p in only_files if p.endswith(extensions)]

if not pictures:
    pictures = "Images not found"

# pictures = []
# for file in only_files:
#     if file.endswith(extensions):
#         pictures.append(file)

print(pictures)
