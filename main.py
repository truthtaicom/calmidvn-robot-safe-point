import numpy as np
import matplotlib.pyplot as plt

origin_x, origin_y = 100, 100
x_s = np.arange(-origin_x, origin_y+1, 1)
y_s = np.arange(-origin_x, origin_y+1, 1)
safe_number = 23 # points are safe that are less than or equal to 23
safe_area_name = 'really_safe_point'

'''
To find all access points that the robot can go. We need to follow some steps:

1. Try to look at all points on the grid to check if it is safe. we named "really_safe_point"
2. From a really_safe_point, we can go **UP (x,y+1)**, **DOWN (x, y-1)**, **LEFT (x-1, y)**, **RIGHT (x+1, y)** to check if any these points is "really_safe_point"
3. Finally, we should count "really_safe_point" points only
4. Virtualize the Grid
'''

coords = []

def check_is_safe_area(x, y):
  return any([coords[y-1][x] == safe_area_name, coords[y+1][x] == safe_area_name, coords[y][x-1] == safe_area_name, coords[y][x+1] == safe_area_name])

def get_really_safe_point():
  return [[1 if safety == safe_area_name else 0 for safety in x_coords[1:-1]] for x_coords in coords[1:-1]]

def start():
  # 1. Try to look all point on the grid to check if it safe. we named "really_safe_point"
  for y in y_s:
    x_coords = []
    for x in x_s:
        coords_digits_sum = sum([int(i) for i in str(abs(x))]) + sum([int(i) for i in str(abs(y))])
        safe = True if coords_digits_sum <= safe_number else False
        x_coords.append(safe)
    coords.append(x_coords)

  coords[origin_y][origin_x] = safe_area_name

  
  # 2. From a really_safe_point to check if any points is "really_safe_point"
  robot_moving = True
  while robot_moving == True:
      robot_moving = False
      for y,x_coords in enumerate(coords[1:-1], start=1):
          for x,is_safe in enumerate(x_coords[1:-1], start=1):
            if is_safe == safe_area_name: continue
            elif is_safe and check_is_safe_area(x,y):
                coords[y][x] = safe_area_name
                robot_moving = True

def virtualize():
  # 3. Finally, we should count "really_safe_point" points only
  really_safe_points = get_really_safe_point()

  # 4. Virtuallize the Grid
  print(really_safe_points)
  plt.imshow(really_safe_points, cmap='YlGn')
  plt.gca().invert_yaxis()
  plt.title(f"Accessible area: {sum([sum(i) for i in really_safe_points])} / {(origin_x*2)**2}")
  plt.show()


start()
virtualize()