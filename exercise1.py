# Weather and AQI data of Gandhinagar for last 10 days

# Temperature in degree Celsius
temperature = [32, 34, 33, 35, 36, 34, 33, 32, 31, 34]

# Humidity in percentage
humidity = [45, 50, 55, 52, 48, 47, 53, 54, 49, 51]

# AQI values
aqi = [110, 120, 115, 130, 140, 125, 118, 122, 135, 128]


# Function to calculate average
def calculate_average(data):
    return sum(data) / len(data)


# Function to calculate median
def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]

    return median


# Calculate results

temp_avg = calculate_average(temperature)
temp_median = calculate_median(temperature)

hum_avg = calculate_average(humidity)
hum_median = calculate_median(humidity)

aqi_avg = calculate_average(aqi)
aqi_median = calculate_median(aqi)


# Prepare result text

result = f"""
Gandhinagar Weather and AQI Analysis (Last 10 Days)
--------------------------------------------------

Temperature:
Average = {temp_avg}
Median = {temp_median}

Humidity:
Average = {hum_avg}
Median = {hum_median}

AQI:
Average = {aqi_avg}
Median = {aqi_median}
"""


# Print result
print(result)


# Save result to text file

file = open("gandhinagar_weather_aqi_analysis.txt", "w")
file.write(result)
file.close()


print("Results saved successfully in gandhinagar_weather_aqi_analysis.txt")