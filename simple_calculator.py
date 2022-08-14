from gettext import find

def problem_check(prob):  # This function returns a boolean: return false if a char in problem is not a readable char
    #                       for this program to solve.
    chars = "1234567890+-*/^()"
    for characters in prob:
        if characters not in chars:
            return False
    if prob.count('(') != prob.count(')'):
        return False
    index_i = 0
    for i in range(prob.count('(')):
        index_i = prob.find("(", index_i + 1)
        if index_i > 0 and not is_sym(prob[index_i - 1]):
            return False
    prev = False
    for char in prob:
        if is_sym(char) and prev and char != "-":
            return False
        prev = is_sym(char)
    return True


def find_first_sub_str(prob):
    index = int(0)
    for op in range(prob.count("(")):
        index = prob.find('(', index)
    if index == -1:
        return 0
    return index


def number_of_operations(prob):
    sym_op = "+-/*^"
    count = 0
    for i in range(len(prob)):
        if prob[i] in sym_op:
            count += 1 if prob[i] != "-" or (prob[i] == "-" and i > 0 and not is_sym(prob[i-1])) else 0
    return count


def calculate(prob):
    while number_of_operations(prob) > 0:
        first_operator = find_first_operation(prob)
        num1 = find_num1(prob, first_operator)
        num2 = find_num2(prob, first_operator)
        sub_str = prob[num1 + 1:num2]
        prob = prob.replace(sub_str,str(make_one_operation(float(prob[num1+1:first_operator]), float(prob[first_operator + 1:num2]), prob[first_operator])), num1) 
    return prob


def find_num1(prob, index):
    if index >= 0:
        index -= 1
    while index >= 0:
        if not is_sym(prob[index]) or (index == 0 and prob[index] == "-"):
            index -= 1
        else:
            index -= 1
            break
    return index


def find_num2(prob, index):
    while index < len(prob):
        index += 1
        if index == len(prob) or is_sym(prob[index]):
            if index < len(prob) and is_sym(prob[index]) and is_sym(prob[index-1]) and prob[index] == "-":
                continue
            break
    return index


def find_first_operation(prob):
    if "^" in prob:
        return prob.find("^")
    elif "*" in prob or "/" in prob:
        if "*" in prob and "/" in prob:
            if prob.find("*") < prob.find("/"):
                return prob.find("*")
            return prob.find("/")
        return prob.find("*") if "*" in prob else prob.find("/")
    elif "+" in prob or "-" in prob:
        if prob.find("+") < prob.find("-") and prob.find("-") != -1 and prob.find("+") != -1:
            return prob.find("+")
        start_i = 0
        for i in range(prob.count("-")):
            start_i = prob.find("-",start_i + 1)
            if (start_i < prob.find("+") or prob.find("+") == -1) and not is_sym(prob[start_i - 1]) and prob.find("-") != -1 and start_i != 0:
                return prob.find("-",start_i)
            if start_i > prob.find("+"):
                return prob.find("+")
        return prob.find("+")
    return -1


def make_one_operation(num1, num2, op):
    if op == "^":
        return pow(num1, num2)
    elif op == "*":
        return num1*num2
    elif op == "/":
        return num1/num2
    elif op == "+":
        return num1+num2
    elif op == "-":
        return num1-num2


def is_sym(character):
    sym_op = "+-/*^"
    return True if character in sym_op else False

    
print("Hello, This is a simple calculator!")
while True:
    problem = input("Please enter a problem: ")
    for i in range(problem.count(" ")):
        problem = problem.replace(" ", "")
    if not problem_check(problem):
        print("Error: Invalid Problem Format!")
        continue
    starting_index = int()
    while problem.count("(") > 0:
        starting_index = find_first_sub_str(problem)
        sub_prob = problem[starting_index + 1: problem.find(')')]
        problem = problem.replace("("+sub_prob+")", calculate(sub_prob), starting_index)
    answer = calculate(problem)
    print("The Answer is", answer)
    _continue = input("Enter Y to continue. ")
    if _continue == "y" or _continue == "Y":
        continue
    else:
        break
