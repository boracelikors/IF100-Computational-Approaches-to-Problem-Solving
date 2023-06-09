earth_orbit = 300000
distance = 384400000
moon_orbit = 100000
duration_seconds = 0
duration_minutes = 0
duration_hours = 0
duration_days = 0


earth_orbit_speed = int(input("Please enter the average take-off velocity (m/s): "))    
speed_between = int(input("Please enter the average flight velocity (m/s): "))
moon_orbit_speed = int(input("Please enter the average landing velocity (m/s): "))

duration_earth = earth_orbit/earth_orbit_speed
duration_between = distance/speed_between
duration_moon = moon_orbit/moon_orbit_speed
duration_seconds = duration_earth + duration_between + duration_moon
int_seconds = int(duration_seconds)



duration_days = int(int_seconds // 86400)
int_seconds = int(int_seconds - duration_days*86400)
duration_hours = int((int_seconds // 3600))
int_seconds = int(int_seconds - (duration_hours)*3600)
duration_minutes = int(int_seconds//60)


duration_seconds = duration_seconds%60

duration_seconds = round(duration_seconds,2)

if (duration_seconds%1) == 0:
  duration_seconds = "{}.00".format(int(duration_seconds))




print("The mission will take {} day(s), {} hour(s), {} minute(s), {} second(s).".format(duration_days,duration_hours,duration_minutes,duration_seconds))
