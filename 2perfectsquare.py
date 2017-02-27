#There is only one three digit number with all the following properties:

#If you replace one of its three digits with '1', you get a square number.
#If you replace another of its digits with '2', you get twice a square number.
#If you replace its other digit with '3', you get three times a square number.

#Each replacement is separate, and uses the original number:
#If you replace the '6' in '366' with 1 to get 361 (19*19)
#after replacing another digit with '2' you would get '266' or '326', not '261' or '321'.


list_of_squares = []
list_of_squares_doubled = []
list_of_squares_tripled = []
max_square = 10
square_number = 10
#create the lists of squares, squares doubles, and squares tripled
#we only want three digit numbers. SO, while loop will stop when we get to 999
while square_number < 1000:
    square_number = max_square **2
    list_of_squares.append(square_number) #creates list of suare numbers
    if square_number*2 < 1000: #only add squares  doubled if it is a three digit number
        list_of_squares_doubled.append(square_number*2)
    if square_number*3 < 1000: #only add squares tripled if it is a three digit number
        list_of_squares_tripled.append(square_number*3)
    max_square += 1



def change_digit(place_value, number, value_change):
    str_number = str(number)
    list_number = list(str_number)
    list_number[place_value]= value_change
    joined_list="".join(list_number)
    return int(joined_list)


def find_answer():

    for number_testing in range (100, 999):
        for i in range(3): #cycles through the place values of number_testing
            replaced_with_one = change_digit(i,number_testing, "1") # changes the place value "i" to a 1
            if replaced_with_one in list_of_squares: # if the new number (relplace_with_one) is a perfect square then check next requirement
                for x in range(3): # cycles through the place values of number_testing
                    if x != i: # makes sure we will not replace the same place value that was replaced with a 1
                        replaced_with_two = change_digit(x, number_testing, "2") #calls function to change place value x to a 2
                        if replaced_with_two in list_of_squares_doubled: #checks if new number(replaced_with_two) is a perfect square times 2
                            for z in range(3): # cycles through the place values of number_testing
                                if z != i and z != x: # makes sure we will not replace a place value that was already replaced
                                    replace_with_three = change_digit(z,number_testing, "3") # calls function to change place value z to a 3
                                    if replace_with_three in list_of_squares_tripled: # chekcs if new number (replace_with_three) is a perfect square times 3
                                        return number_testing   # returns the number that passes all 3 requirements
answer = find_answer()
print ("The answer is:",  answer)
