import vpython


def visualize(dimensions, data):
    # Initialize U object using the first data point.
    if len(data) == 0:
        raise Exception("Empty data.")

    vpython.scene.width = 500
    vpython.scene.height = 600
    vpython.scene.center = vpython.vec(0, u_object.position_m().y / 2, 0)
    thickness = 0.001

    ground = vpython.box(
        pos=vpython.vec(0, 0, 0),
        length=1,
        height=0.01,
        width=thickness)

    base = vpython.box(
        pos=vpython.vec(
            u_object.position_m().x,
            u_object.position_m().y - u_object._center_of_mass_height_m,
            0),
        length=u_object._base_length_m,
        height=thickness,
        width = thickness,
        up=vpython.vec(0, 1, 0))
    side_left = vpython.box(
        pos=vpython.vec(
            u_object.position_m().x - 0.5 * u_object._base_length_m,
            u_object.position_m().y - u_object._center_of_mass_height_m + 0.5 * u_object._side_length_m,
            0),
        length=u_object._side_length_m,
        height=thickness,
        width=thickness,
        up=vpython.vec(1, 0, 0))
    side_right = vpython.box(
        pos=vpython.vec(
            u_object.position_m().x + 0.5 * u_object._base_length_m,
            u_object.position_m().y - u_object._center_of_mass_height_m + 0.5 * u_object._side_length_m,
            0),
        length=u_object._side_length_m,
        height=thickness,
        width=thickness,
        up=vpython.vec(1, 0, 0))

    while True:
        vpython.rate(60)
