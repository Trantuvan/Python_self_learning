import matplotlib.pyplot as plt
from Random_walks import RandomWalk

rw = RandomWalk()
rw.fill_walk()

# Set the size of the plotting window
plt.figure(figsize=(10,6),dpi=128)

plt.plot(rw.x_values,rw.y_values,linewidth = 1, zorder=1)

# Emphasize the first and last points
# vi plot ve ca hinh no se nam de tren first, last poinr
# zorder =2 lon hon set scatter first, last nam tren
plt.scatter(0,0, c='red', edgecolor='none', s=75, zorder=2)
plt.scatter(rw.x_values[-1],rw.y_values[-1], c='green', edgecolor='none', s=75
    , zorder=2)
plt.show()
