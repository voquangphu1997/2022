def print_menu():
    print("""
    Enter your selection: 
    1. translate a word
    2. Exit
 """)
list = {
        'hello': "Xin chao",
        'how': "Nhu the nao",
        'list': "danh sach",
        'dictionary': "tu dien",
        'set': "cai dat",
        'time': "thoi gian"
    }

def translate_word():
    word_input = input("Enter the word to translate: ")
    word_input = word_input.lower()
    if word_input in list:
        print(list[word_input])
       
    else:
        print("The word is none")
        print("Please choose a new word to translate or exit the program")

while True:
    print_menu()
    user_input = int(input("choose your option: "))
    if user_input == 1:
        translate_word()
    elif user_input == 2:
        break