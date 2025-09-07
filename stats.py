def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    num_char_dict = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in num_char_dict:
            num_char_dict[char_lower] = num_char_dict[char_lower] + 1 
        else:   
            num_char_dict[char_lower] = 1
    
    return num_char_dict


def sort_on(items):
    return items["num"]

def sort_dict(unsorted_dict):
    characters = []
    for val in unsorted_dict:
        characters.append({"char":val , "num":unsorted_dict[val]})
    
    characters.sort(reverse=True, key=sort_on)
    return characters