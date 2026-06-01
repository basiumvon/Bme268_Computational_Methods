def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year_input = int(input("Enter a year: "))
print("Is", year_input, "a leap year?", is_leap_year(year_input))