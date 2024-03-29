import math
from dataclasses import dataclass
from u import Vector


@dataclass(kw_only=True)
class State:
    x: float
    y: float
    theta: float


class Simulation:
    def __init__(self, u, time_step_s = 0.001, gravity_m_s2 = -9.81):
        self._u = u
        self._time_step_s = time_step_s
        self._gravity_m_s2 = gravity_m_s2

    def run(self, rate, total_time_s = 1):
        data = []
        t = 0
        i = 0
        while t < total_time_s:
            state = self._propagate()
            if self._u.compute_distance_from_ground() <= 0:
                data.append(state)
                break
            if i % rate == 0:
                data.append(state)
            t += self._time_step_s
            i += 1
        return data

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
