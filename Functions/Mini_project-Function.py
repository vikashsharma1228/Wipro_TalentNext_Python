# Write a Python Function that accepts a hyphen - seperated sequence of colors as input and returns colors in a hyphen - seperated sequence after sorting them in alphabetical order.

def sort_colors(colors):
    colors = colors.split('-')
    colors.sort()
    return '-'.join(colors)


colors = input("Enter the colors: ")
print(sort_colors(colors))