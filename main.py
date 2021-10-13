from itertools import count
from os import stat
import pandas as pd
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import csv 
import statistics
import random 

df = pd.read_csv("studentMarks.csv")
data = df ["Math_score"].tolist()
#fig = ff.create_distplot([data], ["Math Score"], show_hist =False)
#fig.show()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print ("Mean Of Population : ", mean)
print("Standard Deviation of Population :", std_deviation)

def random_set_of_mean (counter):
    dataset = []
    for i in range (0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data [random_index]
        dataset.append(value)
    mean = statistics.mean (dataset)
    return mean 

mean_list = []
for i in range (0,1000):
    set_of_mean =random_set_of_mean(100)
    mean_list.append(set_of_mean)
#mean = statistics.mean(mean_list)
std_deviation = statistics.stdev(mean_list)
print ("Mean Of Sample Distribution : ", mean)
print("Standard Deviation of Sampling Distribution:", std_deviation)

fig = ff.create_distplot([mean_list], ["Student_Marks"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean , mean ],y = [0,0.21], mode = "lines", name = "MEAN"))
fig.show()
first_standard_deviation_start,first_standard_deviation_end = mean - std_deviation , mean + std_deviation
second_standard_deviation_start,second_standard_deviation_end = mean - 2 * std_deviation , mean + 2 * std_deviation
third_standard_deviation_start,third_standard_deviation_end = mean - 3 * std_deviation , mean + 3 * std_deviation
# Data 1 
df=pd.read_csv('data1.csv')
data=df['Math_score'].tolist()
mean_off_sample_one=statistics.mean(data)
print('mean of sample 1',mean_off_sample_one)
fig=ff.create_distplot([mean_list],['student marks'],show_hist=False)
fig.add_trace(go.Scatter(x = [mean , mean ],y = [0,0.21], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_off_sample_one , mean_off_sample_one ],y = [0,0.21], mode = "lines", name = "MEAN OF SAMPLE ONE"))
fig.add_trace(go.Scatter(x=[second_standard_deviation_end, second_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_standard_deviation_end, third_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.add_trace(go.Scatter(x=[first_standard_deviation_end, first_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.show ()
z_score_one = (mean - mean_off_sample_one)/std_deviation
print (z_score_one)

df=pd.read_csv('data2.csv')
data=df['Math_score'].tolist()
mean_off_sample_two=statistics.mean(data)
print('mean of sample 2',mean_off_sample_two)
fig=ff.create_distplot([mean_list],['student marks'],show_hist=False)
fig.add_trace(go.Scatter(x = [mean , mean ],y = [0,0.21], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_off_sample_two , mean_off_sample_two ],y = [0,0.21], mode = "lines", name = "MEAN OF SAMPLE TWO"))
fig.add_trace(go.Scatter(x=[second_standard_deviation_end, second_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_standard_deviation_end, third_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.add_trace(go.Scatter(x=[first_standard_deviation_end, first_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.show ()
z_score_two = (mean - mean_off_sample_two)/std_deviation
print (z_score_two)


df=pd.read_csv('data3.csv')
data=df['Math_score'].tolist()
mean_off_sample_three=statistics.mean(data)
print('mean of sample 2',mean_off_sample_three)
fig=ff.create_distplot([mean_list],['student marks'],show_hist=False)
fig.add_trace(go.Scatter(x = [mean , mean ],y = [0,0.21], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_off_sample_three , mean_off_sample_three ],y = [0,0.21], mode = "lines", name = "MEAN OF SAMPLE three"))
fig.add_trace(go.Scatter(x=[second_standard_deviation_end, second_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_standard_deviation_end, third_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.add_trace(go.Scatter(x=[first_standard_deviation_end, first_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.show ()
z_score_two = (mean - mean_off_sample_three)/std_deviation
print (z_score_two)