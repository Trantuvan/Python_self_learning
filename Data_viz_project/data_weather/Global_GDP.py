import json
import pygal
from pygal.style import RotateStyle as RS
from country_codes import get_country_code
from pygal.maps.world import World

# Load the data into list
filename = r'C:\Users\TRAN TU VAN\Desktop\Python\Data_viz_project\data_weather\GDP.json'
with open(filename) as f:
    gdp_data = json.load(f)

# Build a dictionary of gdp data
cc_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == '2014':
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            # neu code = None vao dict se khong co
            cc_gdp[code] = gdp

# Group the countries into 3 gdp levels
# Less than 5bill, less than 50 bill, >= 50bill
# Also convert to bill for displaying values

cc_gdp_1,cc_gdp_2,cc_gdp_3 = {},{},{}

for cc,gdp in cc_gdp.items():
    if gdp < 5*10**9:
        cc_gdp_1[cc] = round(gdp/10**9)
    elif gdp < 5*10**10:
        cc_gdp_2[cc] = round(gdp/10**9)
    else:
        cc_gdp_3[cc] = round(gdp/10**9)

# See how many countries are in each level
print(len(cc_gdp_1),len(cc_gdp_2),len(cc_gdp_3))

wm_style = RS('#336699')
wm = World(style=wm_style)
wm.title = 'Global GDP in 2014, by country in billion $'
wm.add('0-5bn',cc_gdp_1)
wm.add('5bn-50bn',cc_gdp_2)
wm.add('>50bn',cc_gdp_3)

wm.render_to_file('global_gdp.svg')

