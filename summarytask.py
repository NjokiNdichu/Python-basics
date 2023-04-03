length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))


def surface_area(length,width,height):
    return 2 * (length * width + length * height + width * height)


def volume(length,width,height):
    return length * width * height


sa=surface_area(length,width,height)
vol=volume(length,width,height)
print("The surface area is:", sa)
print("The volume is:", vol)