import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = r'C:\Users\TRAN TU VAN\Desktop\Python\Data_viz_project\data_weather\death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # Print headers and their positions
    # for index, column_header in enumerate(header_row):
    #     print(index,column_header)
    # Extracting and reading data 1st row in reader
    highs,dates, lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])

        except:
            print(current_date,'missing date')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)
# Plot data
fig = plt.figure(dpi=100,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# Plot format
plt.title('Daily high-low temperature-2014\n Death Valley,CA',fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)


plt.show()

