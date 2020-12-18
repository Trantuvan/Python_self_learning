import json
import pygal.maps.world
from pygal.style import LightColorizedStyle as LCS, RotateStyle
from country_codes import get_country_code

# Load the data into a list
filename = r'C:\Users\TRAN TU VAN\Desktop\Python\Data_viz_project\data_weather\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Print the 2010 population for each country
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # Neu xai int truoc se loi do data inconsitence can chuyen float
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        # if code:
        #     print(code+" "+str(population))
        # else:
        #     print('ERROR - ' + country_name)

# Build a dictionary of population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # Neu xai int truoc se loi do data inconsitence can chuyen float
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code]=population
# Group the countries into 3 population levels
cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
for cc,pop in cc_populations.items():
    if pop < 10**7:
        cc_pops_1[cc]=pop
    elif pop < 10**9:
        cc_pops_2[cc]=pop
    else:
        cc_pops_3[cc]=pop

# See how many countries are in each level
# print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

wm_style = RotateStyle('#336699',base_style = LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)


wm.render_to_file('world_population.svg')
