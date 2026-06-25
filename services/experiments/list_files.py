from pathlib import Path

book_folder = Path("../data/Books/Book1")

for file in book_folder.iterdir():
    print(file.name)