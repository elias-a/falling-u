from vpython import scene, box, vec, rate
from u import Vector


def _create_box(length, point, thickness, up):
    return box(
        pos=vec(point.x, point.y, 0),
        length=length,
        height=thickness,
        width = thickness,
        up=up)


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

    base = _create_box(
        dimensions.base_length_m,
        Vector(x=data[0].x, y=data[0].y - dimensions.center_of_mass()),
        thickness,
        vec(0, 1, 0))
    side_left = _create_box(
        dimensions.side_length_m,
        Vector(
            x=data[0].x - dimensions.base_length_m / 2,
            y=data[0].y - dimensions.center_of_mass() + dimensions.side_length_m / 2),
        thickness,
        vec(1, 0, 0))
    side_right = _create_box(
        dimensions.side_length_m,
        Vector(
            x=data[0].x + dimensions.base_length_m / 2,
            y=data[0].y - dimensions.center_of_mass() + dimensions.side_length_m / 2),
        thickness,
        vec(1, 0, 0))

    while True:
        rate(60)
