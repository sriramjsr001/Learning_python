
#this is example of printing 4 different calculation
print(f"10 days are {10*24*60} minutes")
print(f"20 days are {20*24*60} minutes")
print(f"30 days are {30*24*60} minutes")
print(f"40 days are {40*24*60} minutes")

#here we can use variable to save some repetitive work
calculation_to_units = 24
name_of_the_unit = "hours"

print(f"10 days are {10 * calculation_to_units} {name_of_the_unit}")
print(f"20 days are {20 * calculation_to_units} {name_of_the_unit}")
print(f"30 days are {30 * calculation_to_units} {name_of_the_unit}")
print(f"40 days are {40 * calculation_to_units} {name_of_the_unit}")

