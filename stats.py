def number_of_words(book):
    text = book()
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def characters_count (book):
    text = book ()
    lowercase_text = text.lower()
    dict = {}
    for i in lowercase_text:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

def sort_on(items):
    return items["num"]


def sort_func(input_dict):
    new_list = []
    for i in input_dict:
        new_dict = {}
        if i.isalpha():   
            new_dict["char"] = i
            new_dict["num"] = input_dict[i]
            new_list.append(new_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list