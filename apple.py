import csv
from datetime import datetime
import matplotlib.pyplot as plt

file_path = '/content/애플.csv'

december_data = {}

with open(file_path, encoding='CP949') as f:
    data = csv.reader(f)
    header = next(data)
    for row in data:
        date_str = row[0]
        value = float(row[1])

        date = datetime.strptime(date_str, '%Y-%m-%d')
        month = date.month

        if month == 12:
            if 'dates' not in december_data:
                december_data['dates'] = []
            if 'values' not in december_data:
                december_data['values'] = []

            december_data['dates'].append(date_str)
            december_data['values'].append(value)


plt.plot(december_data['dates'], december_data['values'], marker='o', linestyle='-', color='b')
plt.xlabel('date')
plt.ylabel('apple search volume')
plt.title('Apple device search volume from 2018')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()