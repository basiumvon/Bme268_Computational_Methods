def get_fruit_by_color(color):
    fruit_map = {
        "red": "apple",
        "yellow": "banana",
        "green": "kiwi"
    }
    return fruit_map.get(color.lower(), "Unknown fruit")

color_input = input("Enter a fruit color (red, yellow, green): ")
print("The fruit is:", get_fruit_by_color(color_input))