import os
import tomli
from u import U
from simulate import Simulation
#from visualize import visualize
import vpython


try:
    with open(os.path.join(os.path.dirname(__file__), "config.toml"), "rb") as f:
        config = tomli.load(f)
        dimensions_config = config["DIMENSIONS"]
        state_config = config["STATE"]
        base_length_m = config["DIMENSIONS"]["BASE_LENGTH_M"]
        side_length_m = config["DIMENSIONS"]["SIDE_LENGTH_M"]
        position_x_m = config["STATE"]["POSITION_X_M"]
        position_y_m = config["STATE"]["POSITION_Y_M"]
        velocity_x_m_s = config["STATE"]["VELOCITY_X_M_S"]
        velocity_y_m_s = config["STATE"]["VELOCITY_Y_M_S"]
        angular_position_rad = config["STATE"]["ANGULAR_POSITION_RAD"]
        angular_velocity_rad_s = config["STATE"]["ANGULAR_VELOCITY_RAD_S"]
        time_step_s = config["SIMULATION"]["TIME_STEP_S"]
except Exception as e:
    raise Exception()

u_object = U(
    base_length_m=base_length_m,
    side_length_m=side_length_m,
    position_x_m=position_x_m,
    position_y_m=position_y_m,
    velocity_x_m_s=velocity_x_m_s,
    velocity_y_m_s=velocity_y_m_s,
    angular_position_rad=angular_position_rad,
    angular_velocity_rad_s=angular_velocity_rad_s)

#simulation = Simulation(_u, time_step_s=time_step_s)
#data = simulation.run(rate=5)
#visualize(_u, data, rate=5)

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
