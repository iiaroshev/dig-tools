import matplotlib.pyplot as plt
import pandas as pd
url = 'https://raw.githubusercontent.com/ipozdeev/it-skills-for-research/master/data/coding-environment-exercise.csv'
df = pd.read_csv(url)

x = df.date
y = df.value

#making up the plot
plt.plot(x,y)
plt.gcf().autofmt_xdate()

plt.show()

plt.savefig('first plot.jpg', bbox_inches='tight', dpi=150)
