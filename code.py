import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv("./istherecorrelation.csv", sep=";")

# Years
years=data.iloc[:,0]

# WO
wo = data.iloc[:,1]
for i in range(0, len(wo)):
    wo[i] = float(wo[i].replace(',','.'))

# Beer consumption
beer_cons=data.iloc[:,2]

fig, axs = plt.subplots(1, 2)
axs[0].set_title('Number of students in the Netherlands [2006-2018]')
axs[0].set_xlabel('Year')
axs[0].set_ylabel('Students WO[x1000]')
axs[0].plot(years, wo)

axs[1].set_title('Beer consumption in the Netherlands [2006-2018]')
axs[1].set_xlabel('Year')
axs[1].set_ylabel('Beer consumption [x1000 hectoliter]')
axs[1].plot(years, beer_cons)

plt.show()
