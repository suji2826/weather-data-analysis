import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt(
   'weather_data.csv', 
    delimiter=',', 
    skip_header=1)
days = data[:, 0]
temperature = data[:, 1]
humidity = data[:, 2]
rainfall = data[:, 3]
print("Days:", days)
print("Temperature:", temperature)
print("Humidity:", humidity)
print("Rainfall:", rainfall)
print("\n" + "=" * 40)
print("     WEATHER DATA ANALYSIS REPORT")
print("=" * 40)

#TEMPERATURE ANALYSIS
average_temperature = np.mean(temperature)
maximum_temperature = np.max(temperature)
minimum_temperature = np.min(temperature)
print("\nTEMPERATURE ANALYSIS:")
print("Average Temperature:",round(average_temperature,2),"°C")
print("Maximum Temperature:", maximum_temperature,"°C")
print("Minimum Temperature:", minimum_temperature,"°C")

#HUMIDITY ANALYSIS
average_humidity = np.mean(humidity)
maximum_humidity = np.max(humidity)
minimum_humidity = np.min(humidity)
print("\nHUMIDITY ANALYSIS:")
print("Average Humidity:",round(average_humidity,2),"%")
print("Maximum Humidity:", maximum_humidity,"%")
print("Minimum Humidity:", minimum_humidity,"%")

#RAINFALL ANALYSIS
average_rainfall = np.mean(rainfall)
maximum_rainfall = np.max(rainfall)
minimum_rainfall = np.min(rainfall)
print("\nRAINFALL ANALYSIS:")
print("Average Rainfall:",round(average_rainfall,2),"mm")
print("Maximum Rainfall:", maximum_rainfall,"mm")
print("Minimum Rainfall:", minimum_rainfall,"mm")
print("\n" + "=" * 40)

#TEMPERATURE  PLOT
plt.figure(figsize=(8, 5))
plt.plot(days, temperature, marker='o')
plt.title("Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
#plt.grid(True)
plt.show()

#HUMUDITY PLOT
plt.figure(figsize=(8, 5))
plt.plot(days, humidity, marker='o', color='orange')
plt.title("Humidity Trend")
plt.xlabel("Day")
plt.ylabel("Humidity (%)")
#plt.grid(True)
plt.show()

#RAINFALL PLOT
plt.figure(figsize=(8, 5))
plt.plot(days, rainfall, marker='o', color='green')
plt.title("Rainfall Trend")
plt.xlabel("Day")
plt.ylabel("Rainfall (mm)")
#plt.grid(True)
plt.show()

# Weather Classification
print("\nWEATHER CLASSIFICATION")
print("-" * 30)
for i in range(len(temperature)):
    if temperature[i] > 33:
        category = "Hot"
    elif temperature[i] < 28:
        category = "Cool"
    else:
        category = "Normal"
    print(f"Day {int(days[i])}: {category}")
