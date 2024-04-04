from vpython import scene, box, compound, vec, rate, cos, sin


def vec_2d(x, y):
    return vec(x, y, 0)


def _create_box(length, thickness, up):
    return box(length=length, height=thickness, width=thickness, up=up)


def visualize(dimensions, data, rate_):
    # Initialize U object using the first data point.
    if len(data) == 0:
        raise Exception("Empty data.")

    # Create the scene and center on the midpoint between the ground and 
    # the starting point of the object.
    scene.width = 500
    scene.height = 600
    scene.center = vec(0, data[0].y / 2, 0)
    # The object is modeled with thin height and width. This value is
    # purely for visual purposes.
    thickness = 0.005

    ground = _create_box(1, thickness, vec(0, 1, 0))
    base = _create_box(dimensions.base_length_m, thickness, vec(0, 1, 0))
    left_side = _create_box(dimensions.side_length_m, thickness, vec(1, 0, 0))
    right_side = _create_box(dimensions.side_length_m, thickness, vec(1, 0, 0))

    base.pos = vec_2d(x=data[0].x, y=data[0].y - dimensions.center_of_mass())
    y = data[0].y - dimensions.center_of_mass() + dimensions.side_length_m / 2
    left_side.pos = vec_2d(x=data[0].x - dimensions.base_length_m / 2, y=y)
    right_side.pos = vec_2d(x=data[0].x + dimensions.base_length_m / 2, y=y)
    u = compound(
        [base, left_side, right_side],
        origin=vec_2d(data[0].x, data[0].y),
        pos=vec_2d(0, 1),
        up=vec_2d(-sin(data[0].theta), cos(data[0].theta)))

    for point in data:
        rate(rate_)
        u.pos = vec_2d(x=point.x, y=point.y)
        u.up = vec_2d(-sin(data[0].theta), cos(data[0].theta))
