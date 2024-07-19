UnitName = 'hours'
calculation_to_units = 24

def days_to_unit(number_of_days):
    # print(number_of_days > 0)
    # if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days * calculation_to_units} {UnitName}"
    # elif number_of_days == 0: 
    #     return "That's a zero!" 

def validate_and_execute():
    try:
        #user_input.isdigit()
        user_input_number = int(number_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number)
            print(calculated_value)
        elif user_input_number == 0: 
            print ("Zero days are zero hours!") 
        else:
            print('Your input is negative number')
    except:
        print('Your input is not a valid number')
user_input = ''
while user_input != 'exit':
    user_input = input("Enter number of days\n")
    for number_of_days_element in set(user_input.split(',')):
        validate_and_execute()
