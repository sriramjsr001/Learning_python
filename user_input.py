calculation_to_unit = 24
name_of_the_unit = "hours"


def day_to_units(num_of_days ):# here we are defining the function & giving parameter as num_of_days
    return f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_the_unit}"

user_input = input("please enter the number of days, ill convert it in to hours\n")
user_input_number=int(user_input)
calculated_value=day_to_units(user_input_number)
print(calculated_value)


