length = int(input("Length of side: "))
width = int(input("Width of side: "))


def area(length, width):
    # code here
    print(length * width)

    if length == width:
        print("Square")


area(length, width)
