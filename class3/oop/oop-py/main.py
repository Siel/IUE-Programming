from shapes import Triangle, Rectangle, Shape

def explicar_shape(shape: Shape):
    print(f"el area del {shape.description()} es {shape.area()} y con color {shape.color()}")

def main():
    t = Triangle(3,6)
    explicar_shape(t)

    r = Rectangle(3,6)
    explicar_shape(r)




    
    


if __name__ == '__main__':
    main()