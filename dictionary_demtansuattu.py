from collections import Counter

def count_number_of_occurence_words_in_message(message_input):
    text_list = message_input.split()
    for i in range(len(text_list)):
        text_list[i] = text_list[i].lower()

    rs = Counter(text_list)
    print(rs)

message_input = input("Enter your message: ")
count_number_of_occurence_words_in_message(message_input)