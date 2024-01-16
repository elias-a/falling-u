import math
from dataclasses import dataclass


@dataclass(kw_only=True)
class Vector:
    x: float
    y: float

    def get_norm(self):
        return math.sqrt(x ** 2 + y ** 2)


class U:
    def __init__(
            self,
            base_length_m = 0.5,
            side_length_m = 0.5,
            position_x_m = 0.,
            position_y_m = 1.,
            velocity_x_m_s = 0.,
            velocity_y_m_s = 0.,
            angular_position_rad = 0.,
            angular_velocity_rad_s = 0.):
        # U dimensions
        self._base_length_m = base_length_m
        self._side_length_m = side_length_m
        self._center_of_mass_height_m = self._compute_center_of_mass()

        # U state
        self._position_m = Vector(
            x=position_x_m,
            y=position_y_m)
        self._velocity_m_s = Vector(
            x=velocity_x_m_s,
            y=velocity_y_m_s)
        self._angular_position_rad = angular_position_rad
        self._angular_velocity_rad_s = angular_velocity_rad_s

    def _get_position_norm(self):
        return position_m.get_norm()

    def _compute_center_of_mass(self):
        return (
            self._side_length_m ** 2 / 
            (2 * self._side_length_m + self._base_length_m))

    def compute_distance_from_ground(self):
        alpha = 2 * math.pi - self._angular_position_rad
        position_norm = self._get_position_norm()
        distance_m = 0

        # TODO: what to do when alpha is 0?
        # TODO: should I use math.atan or math.atan2?

        if 0 < alpha and alpha < math.pi / 2:
            distance_m = (
                math.sqrt(self._base_length_m ** 2 / 4 + 
                    self._center_of_mass_height_m ** 2) * 
                math.atan(self._base_length_m / 2 / 
                    self._center_of_mass_height_m - alpha))
        elif alpha == math.pi / 2:
            distance_m = self._base_length_m / 2
        elif math.pi / 2 < alpha and alpha < math.pi:
            distance_m = (
                math.sqrt(
                    self._base_length_m ** 2 / 4 + 
                    (self._side_length_m - 
                     self._center_of_mass_height_m) ** 2) *
                (math.pi - alpha - 
                 math.atan(self._base_length_m / 2 / 
                    (self._side_length_m - self._center_of_mass_height_m))))
        elif alpha == math.pi:
            distance_m = self._side_length_m + self._center_of_mass_height_m
        else:
            raise Exception("compute_distance_from_ground(): angle not in expected range")

        return position_norm - distance_m
