import geometry_generator as gg

BIGGEST_VALUE = 100000000000000

def get_area_triangle(points: list) -> float:
    return 0.5 * abs(
         (points[0].x * (points[1].y  - points[2].y)) + 
         (points[1].x * (points[2].y  - points[0].y)) +  
         (points[2].x * (points[0].y  - points[1].y))
         )


def  visvalingam_whyatt(points: list, epsilon: float) -> list:
    points[0].not_change = True
    points[len(points) - 1].not_change = True

    found_less_epsilon = False
    first_while = True

    while first_while or found_less_epsilon:
        found_less_epsilon = False
        first_while = False
        min_area = BIGGEST_VALUE
        min_point = None

        for id, point in enumerate(points):
            if point.not_change:
                continue
            
            point.area = get_area_triangle([points[id-1], point, points[id+1]])
            
            if point.area < min_area and point.area < epsilon:
                found_less_epsilon = True
                min_area = point.area
                min_point = point

        if found_less_epsilon:
            print(min_point.id)
            points.remove(min_point)

    return points






if __name__ == "__main__":
    epsilon = 10.0

    # Lines
    x, y = gg.generate_multi_lines(100)
    points = gg.Point.list_xy_to_points(x,y)
    new_points = visvalingam_whyatt(points, epsilon)
    zipped_lists =  gg.Point.list_points_to_lists(new_points)
    nx, ny = zip(*zipped_lists)

    fig,ax = gg.plt.subplots()
    ax.plot(x, y)
    ax.plot(nx, ny)

    id = 0
    for lx, ly in zip(x, y):
        ax.annotate(f'{id}', (lx, ly))
        id += 1
    gg.plt.show()

    # Polygone
    # x, y = gg.draw_polygon(100)
    # points = gg.Point.list_xy_to_points(x,y)
    # new_points = visvalingam_whyatt(points, epsilon)
    # zipped_lists =  gg.Point.list_points_to_lists(new_points)
    # nx, ny = zip(*zipped_lists)

    # fig2,ax2 = gg.plt.subplots()
    # ax2.plot(x, y)
    # ax2.plot(nx, ny)

    # id = 0
    # for lx, ly in zip(x, y):
    #     ax2.annotate(f'{id}', (lx, ly))
    #     id += 1
    # gg.plt.show()