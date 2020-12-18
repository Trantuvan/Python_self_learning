import matplotlib.pyplot as plt

# python assume 1st data point x =0
# but out data x = 1 --> x^2 of 4 = 25
# de sua cung cap du list cua x va list cua y
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares, linewidth=5)

# Set chart title and label axes

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Set size of tick labels

plt.tick_params(axis = 'both', labelsize=14)
# plt.tick_params(direction='out', length=6, width=2, colors='r',
#                grid_color='b', grid_alpha=0.5)

plt.show()
