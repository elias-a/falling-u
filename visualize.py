from vpython import scene, box, vec, rate


def vec_2d(x, y):
    return vec(x, y, 0)


def _sides(p, d):
    y = p.y - d.center_of_mass() + d.side_length_m / 2
    left = vec_2d(x=p.x - d.base_length_m / 2, y=y)
    right = vec_2d(x=p.x + d.base_length_m / 2, y=y)
    return left, right


def _base(p, d):
    return vec_2d(x=p.x, y=p.y - d.center_of_mass())


def _create_box(length, thickness, up):
    return box(length=length, height=thickness, width = thickness, up=up)


def visualize(dimensions, data):
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
    thickness = 0.001

    base = _create_box(dimensions.base_length_m, thickness, vec(0, 1, 0))
    left_side = _create_box(dimensions.side_length_m, thickness, vec(1, 0, 0))
    right_side = _create_box(dimensions.side_length_m, thickness, vec(1, 0, 0))

    base.pos = _base(data[0], dimensions)
    left_side.pos, right_side.pos = _sides(data[0], dimensions)

    while True:
        rate(60)
