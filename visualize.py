import vpython


def visualize(u_object):
    base = vpython.box(
        pos=vpython.vec(
            u_object.position_m().x,
            u_object.position_m().y - u_object._center_of_mass_height_m,
            0),
        length=u_object._base_length_m,
        height=0.001,
        width = 0.001,
        up=vpython.vec(0,1,0))
    side_left = vpython.box(
        pos=vpython.vec(
            u_object.position_m().x - 0.5 * u_object._base_length_m,
            u_object.position_m().y - u_object._center_of_mass_height_m + 0.5 * u_object._side_length_m,
            0),
        length=u_object._side_length_m,
        height=0.001,
        width=0.001,
        up=vpython.vec(1,0,0))
    side_right = vpython.box(
        pos=vpython.vec(
            u_object.position_m().x + 0.5 * u_object._base_length_m,
            u_object.position_m().y - u_object._center_of_mass_height_m + 0.5 * u_object._side_length_m,
            0),
        length=u_object._side_length_m,
        height=0.001,
        width=0.001,
        up=vpython.vec(1,0,0))
    _u = vpython.compound([side_left, side_right, base])
