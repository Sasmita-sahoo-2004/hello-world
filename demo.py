"""Module to calculate the area of a circle."""

def area_of_circle(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): Radius of the circle.

    Returns:
        float: Area of the circle.
    """
    pi = 3.14
    return pi * radius * radius


def main():
    """Main function to print area of a circle with radius 10."""
    r = 10
    area = area_of_circle(r)
    print(area)


if __name__ == "__main__":
    main()
