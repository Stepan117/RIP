from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import arrow

def main():
    print(arrow.now(),"\n")
    r = Rectangle("синего", 14, 14)
    c = Circle("зеленого", 14)
    s = Square("красного", 14)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()