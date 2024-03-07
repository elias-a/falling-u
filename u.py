import math
from dataclasses import dataclass


@dataclass(kw_only=True)
class Vector:
    x: float
    y: float

    def get_norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


@dataclass(kw_only=True, frozen=True)
class ShapeDimensions:
    base_length_m: float
    side_length_m: float

    def center_of_mass(self):
        return (
            self.side_length_m ** 2 / 
            (2 * self.side_length_m + self.base_length_m))


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
        self.dimensions = ShapeDimensions(
            base_length_m=base_length_m,
            side_length_m=side_length_m)

        # U state
        self._position_m = Vector(
            x=position_x_m,
            y=position_y_m)
        self._velocity_m_s = Vector(
            x=velocity_x_m_s,
            y=velocity_y_m_s)
        self._angular_position_rad = angular_position_rad
        self._angular_velocity_rad_s = angular_velocity_rad_s

    def position_m(self, x: float = None, y: float = None):
        if x is not None and isinstance(x, float):
            self._position_m.x = x
        if y is not None and isinstance(y, float):
            self._position_m.y = y
        return self._position_m

    def velocity_m_s(self, v_x: float = None, v_y: float = None):
        if v_x is not None and isinstance(v_x, float):
            self._velocity_m_s.x = v_x
        if v_y is not None and isinstance(v_y, float):
            self._velocity_m_s.y = v_y
        return self._velocity_m_s

    def angular_position_rad(self, theta: float = None):
        if theta is not None and isinstance(theta, float):
            self._angular_position_rad = theta
        return self._angular_position_rad

    def angular_velocity_rad_s(self, omega: float = None):
        if omega is not None and isinstance(theta, float):
            self._angular_velocity_rad_s = omega
        return self._angular_velocity_rad_s

    def _get_position_norm(self):
        return self.position_m().get_norm()


    def compute_distance_from_ground(self):
        alpha = (
            self._angular_position_rad 
            if 0 <= self._angular_position_rad 
                and self._angular_position_rad <= math.pi
            else 2 * math.pi - self._angular_position_rad)
        position_norm = self._get_position_norm()
        distance_m = 0

        # TODO: update paper with alpha=0 equation
        # TODO: should I use math.atan or math.atan2?

        if alpha == 0:
            distance_m = self.dimensions.center_of_mass()
        elif 0 < alpha and alpha < math.pi / 2:
            distance_m = (
                math.sqrt(self.dimensions.base_length_m ** 2 / 4 + 
                    self.dimensions.center_of_mass() ** 2) * 
                math.atan(self.dimensions.base_length_m / 2 / 
                    self.dimensions.center_of_mass() - alpha))
        elif alpha == math.pi / 2:
            distance_m = self.dimensions.base_length_m / 2
        elif math.pi / 2 < alpha and alpha < math.pi:
            distance_m = (
                math.sqrt(
                    self.dimensions.base_length_m ** 2 / 4 + 
                    (self.dimensions.side_length_m - 
                     self.dimensions.center_of_mass()) ** 2) *
                (math.pi - alpha - 
                 math.atan(self.dimensions.base_length_m / 2 / 
                    (self.dimensions.side_length_m - 
                     self.dimensions.center_of_mass()))))
        elif alpha == math.pi:
            distance_m = self.dimensions.side_length_m + self.dimensions.center_of_mass()
        else:
            raise Exception("compute_distance_from_ground(): angle not in expected range")

        return position_norm - distance_m
