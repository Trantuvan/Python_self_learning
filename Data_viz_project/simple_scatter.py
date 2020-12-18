import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
# plt.scatter(x_values,y_values,s=40)
# Remove outlines color default dot blue outline black
# plt.scatter(x_values,y_values,edgecolor='r',s=40)
# Custom color c = 'yellow'
# plt.scatter(x_values,y_values,c='yellow',edgecolor='none',s=40)
# Custom RGB color
# plt.scatter(x_values,y_values,c = (1,0,0.8),edgecolor='none',s=40)
# Using colormap to specify assign color to each point in dataset
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Purples,edgecolor='none',s=40)


# Set chart title and label axes
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Set the range for each axis
plt.axis([0,1100,0,1100000])
# Set size of tick labels
# plt.tick_params(axis='both', which='major', labelsize=14)

# plt.show()
# Save pic automatically replace plt.show() with
plt.savefig('squares_plot.png',bbox_inches='tight')
