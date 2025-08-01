def get_book_text(path):
    with open(path) as file:
        da_book = file.read()
    return da_book

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()
    
