

def arithmetic_arranger(problems, display=False):
    problem_counter = 0
    zeile_1 = ""
    zeile_2 = ""
    zeile_3 = ""
    zeile_4 = ""

    for problem in problems:
        # extracting the data for each problem
        problem_liste = problem.split()
        operand_1 = problem_liste[0]
        operand_2 = problem_liste[2]
        operator = problem_liste[1]
        # error handling
        if not operand_1.isdigit() or not operand_2.isdigit():
            return "Error: Numbers must only contain digits."  
        if operator =="*" or operator == "/":
            return "Error: Operator must be '+' or '-'."
        operand_1_laenge = len(operand_1)
        operand_2_laenge = len(operand_2)
        if operand_1_laenge > 4 or operand_2_laenge > 4:
            return "Error: Numbers cannot be more than four digits."
        # calculation rule
        if operator == "+":
            result = int(operand_1) + int(operand_2)
        if operator == "-":
            result = int(operand_1) - int(operand_2)
        # lengths needed for desired representation
        maximale_operand_laenge = max(operand_1_laenge, operand_2_laenge)
        laenge_zeile = maximale_operand_laenge + 2
        laenge_result = len(str(result))
        # concatination of each row for desired representation
        zeile_1 += " "*(laenge_zeile - operand_1_laenge) + operand_1 + "    "
        zeile_2 += operator + " "*(laenge_zeile - 1 - len(operand_2)) + operand_2 + "    "
        zeile_3 += "-"*laenge_zeile + "    "
        zeile_4 += " "*(laenge_zeile - laenge_result) + str(result) + "    "
        # last error handling
        problem_counter +=1
    if problem_counter > 5:
        return "Error: Too many problems."
    # optional argument handling for displaying the results of each sum
    # [0:-4] is for cutting out the "    " at the end of the last problem to agree with the expected output
    if display == True:
        arranged_problems = zeile_1[0:-4] + "\n" + zeile_2[0:-4] + "\n" + zeile_3[0:-4] + "\n" + zeile_4[0:-4]
    elif display == False:
        arranged_problems = zeile_1[0:-4] + "\n" + zeile_2[0:-4] + "\n" + zeile_3[0:-4] 
    return arranged_problems

print (arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"]) )

