def main():
    book_path = 'books/frankenstein.txt'
    book_text = file_contents(book_path)
    num_words = num_of_words(book_text)
    words_count = words_counting(book_text)
    a_list = turn_to_list(words_count)
    a_list.sort(reverse=True, key=sort_on)
    alpha_only = alphabet_only(a_list)
 #__________________________________________________________   
    print('___Begin report of books/frankenstein.txt___')
    print(f'{num_words} words were found is this document.\n')
    print_a_report(alpha_only)
    print('\n__End report__')
    
def print_a_report(list_of_words):
    for i in list_of_words:
        print(f'The {i["char"]} character was found {i["num"]} times')
    return

def alphabet_only(list_dict):
    alphabet_only_list =[]
    for i in list_dict:
           if i['char'].isalpha():
                alphabet_only_list.append(i)
    return alphabet_only_list

def sort_on(dict):
    return dict["num"]

def turn_to_list(dict):
    dict_list = []
    for key, value in dict.items():
        new_dict = {'char': key, 'num': value}
        dict_list.append(new_dict)
    return dict_list

def num_of_words(text):
    words = text.split()
    return len(words)

def words_counting(text):
    lowered_string = text.lower()
    counted_words = {}
    for i in lowered_string:
        if i in counted_words:
            counted_words[i] += 1
        else:
            counted_words[i] = 1
    return counted_words

def file_contents(path):
    with open(path) as f:
        return f.read()

main()
