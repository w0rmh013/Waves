import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()

width = 500
height = 500
n_waves = 10
wave_length = 25

d_mat = np.zeros((width, height))

for x in range(width):
    for y in range(height):
        d_mat[x, y] = linalg.norm((x - width / 2, y - height / 2))


w = 255 * np.sin(d_mat / wave_length)
an = plt.imshow(w, interpolation='nearest', cmap='gray', animated=True)
i = 0


def update(*args):
    global i
    w = 255 * np.sin(d_mat / wave_length - 2 * i * np.pi / n_waves)
    an.set_array(w)
    i = (i + 1) % n_waves
    return an,


animate = animation.FuncAnimation(fig, update, interval=50)
plt.show()
