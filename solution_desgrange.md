# CS Assignment

-------------

## Research papers

* Fantastic yeasts and where to find them: the hidden diversity of dimorphic fungal pathogens.
Van Dyke MCC1, Teixeira MM2, Barker BM1

* An analysis of the forces required to drag sheep over various surfaces.
J. Harvey, J. Culvenor, W. Payne, S. Cowley, M. Lawrance, D. Stuart, R. Williams less

* The neurocognitive effects of alcohol on adolescents and college students
Donald W Zeigler, Claire C Wang, Richard A Yoast, Barry D Dickinson, Mary Anne McCaffree, Carolyn B Robinowitz, Melvyn L Sterling, Council on Scientific Affairs, American Medical Association


## Growth of students and beer consumption in the Netherlands

![student and beer consumption](./student_beer_nl.png)


```python
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
```
