import perimeter as pr, main as mn

choice = int(input("Что вы хотите посчитать?: 1-квадрат, 2-пярмоугольник, 3-круг."))

if choice == 1:
    print("Ввидете сторону квадрата")
    side = int(input(">>>"))
    print("Площадь квадрата равна:", mn.square_area(side))
    print("Периметр квадрата равен:", pr.square_perimeter(side))

if choice == 2:
    print("Введите стороны прямоугольника")
    height = int(input("A >>>"))
    width = int(input("B >>>"))
    print("Площадь прямоугольника равна:", mn.rectangle_area(height, width))
    print("Периметр квадрата равен:", pr.rectangle_perimeter(height, width))

if choice == 3:
    print("Ввидете радиус круга")
    radius = int(input(">>>"))
    print("Площадь круга равна:", mn.circle_area(radius))
    print("Периметр круга равен:", pr.circle_area(radius))