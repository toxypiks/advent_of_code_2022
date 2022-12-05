from my_dictionary import dicti

def einlesen(input_path):
    input = []
    file_handler = open(input_path,"r")
    input_data_lines = file_handler.readlines()
    for line in input_data_lines:
        formatted_value = line.replace("\n","")
        half_len = int(len(formatted_value)/2)
        first_part = formatted_value[:half_len]
        second_part = formatted_value[half_len :]
        input.append((first_part,second_part))
    return input

def search_for_duplicated_element(string_list):
    char_list = []
    for string_1, string_2 in string_list:
        my_dict = dicti(90)
        for char in string_1:
            my_dict.set(char, value_of_char(char))
        for char_2 in string_2:
            value = my_dict.get(char_2)
            if value != -1:
                char_list.append(value)
                break
    return char_list
                
                


def value_of_char(char):
    if char.islower():
        value = ord(char) - 96
    if char.isupper():
        value = ord(char) - 38
    return value
    

def main():

    data = einlesen("input.txt")
    result = search_for_duplicated_element(data)
    summe =  sum(result)
    print(result)
    print("{} {}".format(len(result),summe))
    
if __name__ == "__main__":
    main()

