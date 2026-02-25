# Weather data of Gandhinagar for last 10 days

# Temperature in degree Celsius
temperature = [32, 34, 33, 35, 36, 34, 33, 32, 31, 34]

# Humidity in percentage
humidity = [45, 50, 55, 52, 48, 47, 53, 54, 49, 51]


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


# Temperature results
temp_avg = calculate_average(temperature)
temp_median = calculate_median(temperature)

# Humidity results
hum_avg = calculate_average(humidity)
hum_median = calculate_median(humidity)


# Display results
print("Gandhinagar Weather Analysis (Last 10 Days)")
print("------------------------------------------")

print("Average Temperature:", temp_avg)
print("Median Temperature:", temp_median)

print()

print("Average Humidity:", hum_avg)
print("Median Humidity:", hum_median)