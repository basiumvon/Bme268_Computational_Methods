messy_string = input("Enter a hyphen-separated string: ")

cleaned_string = messy_string.replace("-", " ")
final_string = cleaned_string.lower()

print("Cleaned string:", final_string)