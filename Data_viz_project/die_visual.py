from die import Die
import pygal
# Create a D6 (six-sided die)
# self = D6-a dice with six-sided
# roll() has 1 argument D6
die_1 = Die(6)
die_2 = Die(6)

# Make some rolls, and store results in a list.
# results = []
# for roll_num in range(50000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
results = [die_2.roll()+die_1.roll() for roll_num in range(10**6)]

# Analyze the results
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# for value in range(2,max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

frequencies = [results.count(value) for value in range(2,die_1.num_sides*die_2.num_sides+1)]

# Making a histogram using pygal
hist = pygal.Bar()

hist.title = 'Results of rolling two D6 + D6 1,000,000 times'
hist.x_labels = [str(i) for i in range(2,die_1.num_sides*die_2.num_sides+1)]
hist.x_title = 'Result'
hist.y_title = 'frequency of Result'

hist.add('D8 + D8',frequencies)
hist.render_to_file('die_visual.svg')


