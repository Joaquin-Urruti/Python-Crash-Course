import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
	rw = RandomWalk(num_points=100_000)

	rw.fill_walk()

	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(15, 9), dpi=100)
	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_values, rw.y_values, c=point_numbers , cmap=plt.cm.Blues, s=0.5, edgecolors='none')
	ax.scatter(0, 0, c='green', s=100, edgecolors='none')
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100, edgecolors='none')
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
	plt.show()

	keep_running = input("Hacer otro random_walk? (y/n): ")
	if keep_running == 'n':
		break