def main():
    value = 0
    flag = True
    print("Welcome to Calculator")
    while(flag == True):
        print( "Current Value: " + str(value))
        print("What would you like to do? \n [A]DD [S]UB [M]UL [D]IV")
        user_input = input()
        if(user_input == 'A'):
            user_input_add = input("How much would you like to add?")
            value += int(user_input_add)
        elif(user_input == 'S'):
            user_input_sub = input("How much would you like to subtract?")
            value -= int(user_input_sub)
        elif(user_input == 'M'):
            user_input_mult = input("How much would you like to multiply by?")
            value *= int(user_input_mult)
        elif(user_input == 'D'):
            user_input_div = input("How much would you like to divide by?")
            value = value/int(user_input_div)
        else:
            flag = False
            print("Invalid input. Exiting Application Now")      
    






if __name__ == '__main__':
    main()