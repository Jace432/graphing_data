import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use("classic")
figure, graph = plt.subplots()
graph.scatter(rw.x_values, rw.y_values, s=15, c=rw.y_values, cmap=plt.cm.winter,
              edgecolors="none")

graph.scatter(0,0, s=50, color="green",
              edgecolors="none")

graph.scatter(rw.x_values[-1], rw.y_values[-1], s=50, color="red",
              edgecolors="none")

plt.show()