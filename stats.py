
def get_book_text(filePath):
    with open(filePath) as f:
        #file_contents = f.read()
        #print(type(file_contents))
        return f.read()

def get_num_words(text):
    words = text.split()
    print(f"Found {len(words)} total words")

def get_letter_counts():
    words = get_book_text("books/frankenstein.txt").lower()
    # print(words)
    track_letters = {}
    for letter in range(0,len(words)):
        # print(words[letter])
        if words[letter] in track_letters:
            track_letters[words[letter]] = track_letters[words[letter]] + 1
        else:
            track_letters[words[letter]] = 1
    return track_letters