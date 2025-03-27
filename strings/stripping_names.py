person_name = " Jose Manuel "
print((f"Printing the name without leading and trailing spaces:"
       f"\n {person_name}"))

print((f"Printing the name with: \n \t leading spaces: {person_name.lstrip()}"
       f"\n \t trailing spaces: {person_name.rstrip()}"
       f"\n \t leading and trailing spaces: {person_name.strip()}"))
