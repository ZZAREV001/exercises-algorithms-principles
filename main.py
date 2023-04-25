from typing import List, Any, Union

import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

df = open("/Users/GoldenEagle/IdeaProjects/Projet-2-bis/PHEME_01_code/symptoms.txt")
lines = df.readlines()
df.close()

# remove /n at the end of each line
for index, line in enumerate(lines):
    lines[index] = line.strip()

df_symptoms = pd.DataFrame(lines, columns=['Symptoms'])
print(df_symptoms)

# count the occurrences of each symptom in df_symptoms
df_occurrences = [df_symptoms[index].value_counts() for index in df_symptoms]
print(df_occurrences)

# display symptoms
plt.hist(df_symptoms, bins=20)
fig = plt.figure()
fig.subplots_adjust(top=4.0)
ax2 = fig.add_subplot(211)
ax2.set_ylabel('Occurrence of a symptom')
ax2.set_title('Symptoms and their occurrences')
plt.show()
