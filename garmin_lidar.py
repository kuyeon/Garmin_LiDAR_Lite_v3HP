import LiDAR_Lite # Used Garmin LiDAR_Lite V3HP
import time

lidar = LiDAR_Lite.LiDAR_Lite() # make object
lidar.connect(1) # i2c bus number 1

# get distance data from the lidar sensor
def Get_Distance():
    dist = lidar.get_distance()
    time.sleep(0.1)
    return dist


try:
    while True:
        data = Get_Distance()
        print("DISTANCE: {}CM".format(data)) # print unit in "cm"

except Exception as e:
    print(e)

finally:
    pass