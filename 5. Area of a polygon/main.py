def polygon_area(polygon_type:int):
    """Calculates the area of the given polygon.
    Supported polygons: 
    1 = Square;
    2 = Rectangle;
    3 = Triangle;

    Args:
        polygon_type (int): Type of polygon given by an integer number.

    Returns:
        float: Calculated area of the given polygon
    """
    if polygon_type == 1:
        x = input("Please, provide the length of one side: ")
        area = float(x)**2
        return area
    elif polygon_type == 2:
        b = input("Please, provide the length of the base: ")
        h = input("Please, provide the height: ")
        area = float(b) * float(h)
        return area
    elif polygon_type == 3:
        b = input("Please, provide the length of the base: ")
        h = input("Please, provide the height: ")
        area = (float(b) * float(h)) / 2
        return area
    else:
        return 0
    

while True:
    try:
        type = int(input("Select the number of the desired polygon to calculate the area:"\
                    "\n1 = Square"\
                    "\n2 = Rectangle"\
                    "\n3 = Triangle\n"))
        print(polygon_area(type))
    except ValueError:
        print("Please provide a valid number")