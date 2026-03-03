import matplotlib.pyplot as plt
import seaborn as sns

#Matplotlib → basic, low-level plotting
#Seaborn → high-level, statistical plots (built on Matplotlib)
#________________________________________________________________-
"""
Matplotlib is a popular Python library used for data visualization.
It is mainly used to create graphs, charts, and plots to represent data visually.
"""
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [5, 7, 6, 8, 10]
plt.scatter(x, y, color="red", marker="+", linewidth=1)
plt.title("Scatter Plot Example")
plt.xlabel("X values",fontsize=12)
plt.ylabel("Y values") #font size for title and x label also
plt.grid(True) # turns on grid lines.
plt.legend() #gives labels 
plt.show()

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("Line Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

import matplotlib.pyplot as plt
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data)
plt.title("Histogram Example")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

import matplotlib.pyplot as plt
labels = ["Python", "Java", "C++", "R"]
sizes = [40, 25, 20, 15]
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Pie Chart Example")
plt.show()

import matplotlib.pyplot as plt
categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 25]
plt.bar(categories, values)
plt.title("Bar Plot Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()


#Line Plot
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#Bar Plot
plt.bar(x, y)
plt.show()

#HistogramUse: data distribution
plt.hist(data)
plt.show()
sns.histplot(data)

#Scatter Plot Use: relationship between two variables
plt.scatter(x, y)
plt.show()

#Box Plot  Use:spread, median, outliers

sns.boxplot(y=data)
#Box plot shows median, quartiles, and outliers.
