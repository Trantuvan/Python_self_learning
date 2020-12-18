import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

mystyle = LS('#333366', base_style = LCS)
chart = pygal.Bar(style = mystyle, x_label_rotation=0, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['System-design-primer','Public-apis','Python-100-Days']

plot_dicts = [
    {'value':110655,'label':'Description of system-design-primer.'},
    {'value':98973,'label':'Description of Public-apis.'},
    {'value':94779,'label':'Description of Python-100-Days.'},
    ]

chart.add('',plot_dicts)
chart.render_to_file('bar_descriptions.svg')


