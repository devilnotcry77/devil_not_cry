import seaborn as sns
from pandas import DataFrame
import matplotlib.pyplot as plt

Data = {'size': [2,4,8,10,30],
        'location': [2,5,1,2,3],
        'price': [18,20,30,40,50]
        }
df = DataFrame(Data,columns=['size','location','price'])
corrMatrix = df.corr()
plot = sns.heatmap(corrMatrix, annot=True)
plot.get_figure().savefig("correlationmatrix.png")