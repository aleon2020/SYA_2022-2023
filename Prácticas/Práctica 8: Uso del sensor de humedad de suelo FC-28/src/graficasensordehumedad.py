import datetime
import pandas as pd
import matplotlib.pyplot as plt

nombredearchivo = "registrodecambiosdehumedad.csv"
data = pd.read_csv(nombredearchivo)

data['Timestamp'] = pd.to_datetime(data['Timestamp'])

dates = data['Timestamp']
dates = dates.tolist()

vals = data['Humedad']
vals = vals.tolist()

plt.plot(dates,vals)
plt.title("Sensor de humedad")
plt.ylabel('Humedad')
plt.xlabel('Tiempo')
plt.xticks(rotation = 'vertical')
plt.show()