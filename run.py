import os
import tomllib
from u import U


try:
    with open(os.path.join(os.path.dirname(__file__), "config.toml"), "rb") as f:
        config = tomllib.load(f)
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
except Exception as e:
    raise Exception()

_u = U(
    base_length_m=base_length_m,
    side_length_m=side_length_m,
    position_x_m=position_x_m,
    position_y_m=position_y_m,
    velocity_x_m_s=velocity_x_m_s,
    velocity_y_m_s=velocity_y_m_s,
    angular_position_rad=angular_position_rad,
    angular_velocity_rad_s=angular_velocity_rad_s)
