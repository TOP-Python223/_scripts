def polygon_perimeter(point1: tuple,
                      point2: tuple,
                      point3: tuple, /, 
                      *points) -> float:
    """Расчитывает периметр многоугольника, заданного с помощью точек на плоскости."""
    # print(points)
    points = (point1, point2, point3) + points
    # print(points)
    perimeter = 0
    for i in range(len(points)):
        x1 = points[i-1][0]
        y1 = points[i-1][1]
        x2 = points[i][0]
        y2 = points[i][1]
        perimeter += ((x2 - x1)**2+(y2 - y1)**2)**0.5
    return perimeter

p1 = polygon_perimeter((0,0), (0,1), (1,1), (1,0))
print(f'\nПериметр многоугольника {p1:.2f} см')

p2 = polygon_perimeter((0,0), (1,1), (1,0))
print(f'\nПериметр многоугольника {p2:.2f} см')
