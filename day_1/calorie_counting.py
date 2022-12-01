def einlesen(input_path):
    file_handler = open(input_path,"r")
    input_data_lines = file_handler.readlines()

    new_elve = []
    all_input = []

    for line in input_data_lines:
        formatted_line = line.replace("\n",'')
        if formatted_line != '':
            new_elve.append(int(formatted_line))
        else:
            all_input.append(new_elve)
            new_elve = []
    all_input.append(new_elve)
    return all_input


def calorie_counting(input_data):
    highest_amount1 = -1
    highest_amount2 = -1
    highest_amount3 = -1
    for data in input_data:
        sum_akku = 0
        for number in data:
            sum_akku += number
        if sum_akku > highest_amount1:
            highest_amount3 = highest_amount2
            highest_amount2 = highest_amount1
            highest_amount1 = sum_akku
        elif sum_akku > highest_amount2:
            highest_amount3 = highest_amount2
            highest_amount2 = sum_akku
        elif sum_akku > highest_amount3:
            highest_amount3 = sum_akku    
    return (highest_amount1 + highest_amount2 + highest_amount3)
        
        

def main():
    input_data = einlesen("input.txt")
    highest_calorie_count = calorie_counting(input_data)
    print(highest_calorie_count)
    

            
if __name__ == "__main__":
    main()
        
