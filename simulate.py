import math
from math import tan, sin, cos, atan, pi
from dataclasses import dataclass, astuple
from u import Vector


@dataclass(kw_only=True)
class State:
    x: float
    y: float
    theta: float

    def __iter__(self):
        return iter(astuple(self))


class Simulation:
    def __init__(
        self,
        u,
        time_step_s=0.001,
        stopping_velocity=1e-4,
        surface_factor=0.85,
        gravity_m_s2=-9.81,
    ):
        self._u = u
        self._time_step_s = time_step_s
        self._stopping_velocity = stopping_velocity
        self._surface_factor = surface_factor
        self._gravity_m_s2 = gravity_m_s2

    def run(self, rate):
        data = [
            State(
                x=self._u.position_m().x,
                y=self._u.position_m().y,
                theta=self._u.angular_position_rad(),
            ),
        ]
        i = 0
        while True:
            state = self._propagate()
            if self._u.compute_distance_from_ground() <= 0 and self._u.velocity_m_s().y < 0:
                data.append(state)
                self._apply_impulse()
                self._apply_torque()
                if abs(self._u.velocity_m_s().y) < self._stopping_velocity:
                    break
            if i % rate == 0:
                data.append(state)
            i += 1
        return data

    def _apply_impulse(self):
        self._u.velocity_m_s().y *= -self._surface_factor

    def _apply_torque(self):
        h = self._u.dimensions.side_length_m
        c = self._u.dimensions.center_of_mass()
        b = self._u.dimensions.base_length_m / 2
        theta = self._u.angular_position_rad()
        x = (h-c-b*tan(pi/2-theta)) * cos(theta)
        y = self._u.position_m().y
        z = Vector(x=x, y=y)
        v = atan(x/y)
        alpha = self._gravity_m_s2 * sin(v) / z.get_norm()
        updated_omega = self._u.angular_velocity_rad_s() + alpha*0.01
        self._u.angular_velocity_rad_s(omega=updated_omega)

    def _propagate(self):
        # Update position.
        x_m = (
            self._u.position_m().x + 
            self._u.velocity_m_s().x * self._time_step_s)
        y_m = (
            self._u.position_m().y +
            self._u.velocity_m_s().y * self._time_step_s + 
            0.5 * self._gravity_m_s2 * self._time_step_s ** 2)
        self._u.position_m(x=x_m, y=y_m)

        # Update velocity.
        v_y_m_s = (
            self._u.velocity_m_s().y + 
            self._gravity_m_s2 * self._time_step_s)
        self._u.velocity_m_s(v_y=v_y_m_s)

        # Update angular position.
        theta_rad = (
            self._u.angular_position_rad() + 
            self._u.angular_velocity_rad_s() * self._time_step_s) % (2 * math.pi)
        self._u.angular_position_rad(theta=theta_rad)

        return State(x=x_m, y=y_m, theta=theta_rad)
