from plotly.graph_objs import Bar, Layout
from plotly import offline
from random import randint
from collections import Counter

names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]

names2 = []


for name in range(100):
    names2.append(names[randint(0,4)])

frequency = Counter(names2)


#x_values = list(range(1,len(names)+1))
data = [Bar(x=names, y=[frequency[name] for name in names])]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of number of repeating names',xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d7.html')


max_frequency = max(frequency.values())
for name,count in frequency.items():
    if count == max_frequency:
        print(name + " has frequency " + str(count))
