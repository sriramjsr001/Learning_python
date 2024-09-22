calculation_to_unit = 24
name_of_the_unit = "hours"


def day_to_units(num_of_days ):# here we are defining the function & giving parameter as num_of_days
    print(num_of_days > 0)#here we are checking the condition so in out put it will show true if the provided input is true otherwise it will show false
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_the_unit}"
def validate_and_execute():
    if user_input.isdigit():  # this function is for ensuring the entered number is digit
        user_input_number = int(user_input)
        calculated_value = day_to_units(user_input_number)
        print(calculated_value)
    else:
        print("please enter the valid number to continue the program")

user_input = input("please enter the number of days, ill convert it in to hours\n")
validate_and_execute()





