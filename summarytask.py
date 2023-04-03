length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))


def surface_area():
    surfacearea=2 * (length * width + length * height + width * height)
    print("The surface area is:", surfacearea)

surface_area()

def volume():
    vol=length * width * height
    print("The volume is:", vol)


volume()