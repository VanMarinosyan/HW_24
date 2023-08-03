# HW_1

def generate_christmas_tree(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))

generate_christmas_tree(5)
