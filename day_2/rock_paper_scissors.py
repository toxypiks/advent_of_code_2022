# (A,X)Rock=1 (B,Y)Paper =2 (C,Z)Scissors=3
# lose=0 draw=3 win=6

# (A,X) -> (0,3) 

def einlesen(input_path):
    inputs = []
    file_handler = open(input_path,"r")
    input_data_lines = file_handler.readlines()
    for line in input_data_lines:
        first = line[0]
        second = line[2]
        inputs.append((first,second))
    return inputs    

def calculate_score(rules,inputs):
    score = 0
    for input in inputs:
        (first, second) = rules[input]
        sum_round = first + second
        score += sum_round
    return score
    


def main():
    rules = {
        ('A','X') : (1,3),
        ('A','Y') : (2,6),
        ('A','Z') : (3,0),
        ('B','X') : (1,0),
        ('B','Y') : (2,3),
        ('B','Z') : (3,6),
        ('C','X') : (1,6),
        ('C','Y') : (2,0),
        ('C','Z') : (3,3)
    }
    data = einlesen("input.txt")
    tournament_score = calculate_score(rules,data)
    print(tournament_score)

if __name__ == "__main__":
    main()
