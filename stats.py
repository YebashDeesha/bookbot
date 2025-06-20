import sys
def get_book_text(filepath):
    with open(filepath) as f:
        file_conent = f.read()

    return file_conent   
def sort_on(item):
        return item[1]
def get_character_count(filepath):
    x = get_book_text(filepath).lower()
    character_count: dict[str, int] = {} 
    for line in x:
        for char in line:
            if char.isalpha():
                if char not in character_count:
                    character_count[char] = 0
                character_count[char] += 1

    sorted_characters = sorted(character_count.items(), key=sort_on, reverse=True)
    return sorted_characters
    

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath).splitlines()
    num_words = sum(len(line.split()) for line in book_text)
    #print(f"{num_words} words found in the document")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in get_character_count(filepath):
        print(f"{char[0]}: {char[1]}")
    print("============= END ===============")
