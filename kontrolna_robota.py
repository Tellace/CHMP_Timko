import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from scipy.interpolate import interp1d

def part_1():
    speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]
    np_speed = np.array(speed)
    time = np.linspace(start=0, stop=11, num=12)

    print(time)

    plt.plot(time, np_speed, marker="o", color='green', )
    plt.axis([0, 11, 0, 130])
    plt.grid()
    plt.show()

def task(kind: str):
    f_linear = interp1d(x=time, y=np_speed, kind=kind)
    new_time = np.linspace(start=0, stop=11, num=10_000)
    new_np_speed = f_linear(new_time)

    plt.plot(new_time, new_np_speed, 'r', time, np_speed, 'bo')
    plt.axis([0, 11, 0, 130])
    plt.grid()
    plt.show()

    s = integrate.quad(lambda x: f_linear(x), 0, 11)
    print(f"S={s[0]}")

    task("cubic")
    task("quadratic")

if __name__ == '__main__':
    part_1()