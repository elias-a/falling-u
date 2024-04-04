from vpython import scene, box, compound, vec, rate, cos, sin


def vec_2d(x, y):
    return vec(x, y, 0)


def visualize(dimensions, data, rate_):
    # Initialize U object using the first data point.
    if len(data) == 0:
        raise Exception("Empty data.")
    x, y, theta = data[0]

    # Create the scene and center on the midpoint between the ground and 
    # the starting point of the object.
    scene.width = 500
    scene.height = 600
    scene.center = vec(0, y / 2, 0)
    # The object is modeled with thin height and width. This value is
    # purely for visual purposes.
    thickness = 0.005
    ground = box(length=1, height=thickness, width=thickness, up=vec_2d(0, 1))
    u = compound(
        [
            box(
                length=dimensions.base_length_m,
                height=thickness,
                width=thickness,
                up=vec_2d(0, 1),
                pos=vec_2d(x, y - dimensions.center_of_mass()),
                visible=False,
            ),
            box(
                length=dimensions.side_length_m,
                height=thickness,
                width=thickness,
                up=vec_2d(1, 0),
                pos=vec_2d(
                    x - dimensions.base_length_m / 2,
                    y - dimensions.center_of_mass() + 
                        dimensions.side_length_m / 2
                ),
                visible=False,
            ),
            box(
                length=dimensions.side_length_m,
                height=thickness,
                width=thickness,
                up=vec_2d(1, 0),
                pos=vec_2d(
                    x + dimensions.base_length_m / 2,
                    y - dimensions.center_of_mass() + 
                        dimensions.side_length_m / 2
                ),
                visible=False,
            ),
        ],
        origin=vec_2d(x, y),
        up=vec_2d(-sin(theta), cos(theta)),
        pos=vec_2d(x, y))

    for point in data[1:]:
        rate(rate_)
        u.pos = vec_2d(point.x, point.y)
        u.up = vec_2d(-sin(point.theta), cos(point.theta))
