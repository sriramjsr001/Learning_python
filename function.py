calculation_to_unit=24
name_of_the_unit="hours"

def day_to_units(num_of_days,custom_massage):#here we are defining the function & giving parameter as num_of_days
    print(f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_the_unit}")
    print(custom_massage)

day_to_units(32,"days are converted to hours-Good to go!!!") #we are calling the function & giving inputs
    
