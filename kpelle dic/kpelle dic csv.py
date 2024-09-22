import pandas as pd

encoding = 'utf-8'  

with open('kpelle dic.txt', encoding=encoding) as file:
    data = file.readlines()

lemmas = []
pos = []
defeng = []

for i in range(0, 6612, 3): 
    lemmas.append(data[i].strip())
    pos.append(data[i + 1].strip())
    defeng.append(data[i + 2].strip())

df = pd.DataFrame({'Lemma': lemmas, 'PoS': pos, 'DefEng': defeng})

df.to_csv('kpelle dic.csv', index=False, encoding=encoding)