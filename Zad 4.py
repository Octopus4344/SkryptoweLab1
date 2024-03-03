def area_of_triangle(base, height):
    if base > 0 and height > 0:
        return base * height / 2
    else:
        print('Incorrect value')
        return None


def ui():
    base = input("Enter the base: ")
    height = input("Enter the height: ")
    try:
        print(f'The are of a given triangle is: {area_of_triangle(int(base), int(height))}')
    except ValueError:
        print('Value is of an incorrect type')


ui()
