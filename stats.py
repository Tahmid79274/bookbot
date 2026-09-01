
def sort_on(item: tuple[str, int]) -> int:
    return item[0]

def chars_dict_to_sorted_list(dictionary: dict[str, int]) -> list[tuple[str, int]]:
    new_list = []
    print(f'Dictionary:{dictionary}')
    for key in dictionary:
        print(f"{str(key)} = {dictionary[key]}")
        new_list.append((dictionary[key],(str(key))))
    return sorted(new_list, reverse=True,key=sort_on)

def get_book_text(filePath):
    with open(filePath) as f:
        #file_contents = f.read()
        #print(type(file_contents))
        return f.read()

def get_num_words(text):
    words = text.split()
    print(f"Found {len(words)} total words")

def get_letter_counts(path):
    words = get_book_text(path).lower()
    # print(words)
    track_letters = {}
    for letter in range(0,len(words)):
        # print(words[letter])
        if words[letter] in track_letters:
            track_letters[words[letter]] = track_letters[words[letter]] + 1
        else:
            track_letters[words[letter]] = 1
    return track_letters

def get_sorted_report(letter_counts,path):
    dictionary_list = []
    print("============ BOOKBOT ============\n----------- Word Count ----------")
    get_num_words(get_book_text(path))
    print("--------- Character Count -------")
    for key in letter_counts.keys():
        dictionary_list.append({
            "char": key,
            "num": letter_counts[key]
        })
    # print(dictionary_list)
    dictionary_list.sort(reverse= True, key=sort_on)
    # print("=========================================")
    # print(dictionary_list)
    for dictionary in dictionary_list:
        if dictionary['char'].isalpha():
            print(f"{dictionary['char']}: {dictionary['num']}")
    print("============= END ===============")



def num_words(content):
    return len(content.split())

def letter_count_dic(content):
    record = dict()
    for letter in content:
        if letter in record.keys():
             record[letter] += 1
        else:
            record[letter] = 1
    return record

def sorted_report(dictionary):
    sorted_record = []
    for key in dictionary.keys():
        sorted_record.append(
            {
                "char" : key,
                "num" : dictionary[key]
            }
        )
    sorted_record.sort(reverse=True,key=sorts_on)
    return sorted_record

def sorts_on(items):
    return items["num"]
