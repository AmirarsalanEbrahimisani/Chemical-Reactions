import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation

manual_data = {
    "Name": ["Coral", "Zebrafish", "Fingerprint", "Bacteria 1"],
    "Du": [0.16, 0.16, 0.19, 0.16],
    "Dv": [0.08, 0.08, 0.05, 0.08],
    "f": [0.060, 0.035, 0.060, 0.035],
    "k": [0.062, 0.060, 0.062, 0.065],
}
df = pd.DataFrame(manual_data)
print(df.iloc[2, :])


def laplacian(z):
    left = np.roll(z, 1, axis=1)
    right = np.roll(z, -1, axis=1)
    up = np.roll(z, 1, axis=0)
    down = np.roll(z, -1, axis=0)

    return (left + right + up + down) - 4 * z


def update(u, v, Name="Coral", Du=0.16, Dv=0.08, f=0.060, k=0.062, dt=0.2):
    Lu = laplacian(u)
    Lv = laplacian(v)

    reaction = u * v**2

    diff_u = Du * Lu - reaction + f * (1.0 - u)
    diff_v = Dv * Lv + reaction - (f + k) * v

    u_new = u + diff_u * dt
    v_new = v + diff_v * dt

    return np.clip(u_new, 0, 1), np.clip(v_new, 0, 1)


u_list, v_list = np.ones((100, 100)), np.zeros((100, 100))

v_list[100 // 2 - 5 : 100 // 2 + 5, 100 // 2 - 5 : 100 // 2 + 5] = 0.25
u_list[100 // 2 - 5 : 100 // 2 + 5, 100 // 2 - 5 : 100 // 2 + 5] = 0.5

fig, ax = plt.subplots(figsize=(8, 8))
im = ax.imshow(v_list, cmap="magma", animated=True)
ax.axis("off")


def animate(frame):
    global u_list, v_list
    for _ in range(100):
        u_list, v_list = update(u_list, v_list, **df.iloc[2, :].to_dict())

    im.set_array(v_list)
    return [im]


ani = FuncAnimation(fig, animate, frames=100, interval=20, blit=True)

plt.show()
