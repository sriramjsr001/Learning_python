calculation_to_unit = 24
name_of_the_unit = "hours"


def day_to_units(num_of_days ):# here we are defining the function & giving parameter as num_of_days
    return f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_the_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = day_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you have entered 0 please enter a positive number")
        

    except:
        print("please enter the valid number to continue the program")


user_input = ""


while user_input != "exit":
    user_input = input("please enter the number of days, ill convert it in to hours\n")
    for num_of_days_element in user_input.split(","):
        validate_and_execute()