length = float(input("Enter the length of the cube: "))
def surface_area(length):
    return 6*(length**2)


def volume(length):
    return length**3


sa=surface_area(length)
vol=volume(length)
print("The surface area is:", sa)
print("The volume is:", vol)