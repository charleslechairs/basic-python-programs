# 1 - Write a Function speed alert with two args speed and limits speed_alert(speed,**limits), default speed limit = 60, if kwargs contain city limit or highway limit apply them accordingly, return ok or overspeed
def speed_alert(speed, **limits):
    speed_limit = 60
    if 'city_limit' in limits:
        speed_limit = limits['city_limit']
    elif 'highway_limit' in limits:
        speed_limit = limits['highway_limit']
    if speed > speed_limit:
        return "overspeed" 
    else:
        return "ok"
# 2 - Design a function battery health parameters voltage current and temp, calc power, if temp > 45 degrees or voltage < 3.2V warn unsafe conditions, return power and status
def battery_health(voltage, current, temp):
    power = voltage * current
    if temp > 45 or voltage < 3.2:
        status = "unsafe conditions"
    else:
        status = "safe"
    return power, status
# 3 - Create an F1 race performance function f1_performance(lap_time, weather, **race_conditions), default tire compound = 'medium', default fuel_level = 50kg, 
#  if kwargs contain tire_compound (soft/medium/hard)
# adjust lap time by -2s/0s/+1.5s respectively, if kwargs contain fuel_level and it's below 20kg warn 'low fuel', if weather is 'rain' add 3s to lap time, return final lap time and any warnings
def f1_performance(lap_time, weather, **race_conditions):
    warnings = []
    tire_compound = race_conditions.get("tire_compound", "medium")
    fuel_level = race_conditions.get("fuel_level", 50)

    if tire_compound == "soft":
        lap_time -= 2
    elif tire_compound == "hard":
        lap_time += 1.5

    if fuel_level < 20:
        warnings.append("low fuel")

    if weather == "rain":
        lap_time += 3

    return lap_time, warnings

print(speed_alert(70, city_limit=50))  # Example usage
print(battery_health(3.5, 10, 40))      # Example usage 
print(f1_performance(90, 'rain', tire_compound='soft', fuel_level=15))  # Example usage