import numpy as np
import matplotlib.pyplot as plt
import cv2

def get_line(A,B):
  x1,y1,x2,y2 = A[0],A[1],B[0],B[1]
  m = (y2-y1)/(x2-x1)
  c = y1 - m * x1
  return m,c

def check_for_obstacle_1(points,point):
  count = 0
  i = 0
  x,y = point[0],point[1]
  m1,c1 = get_line(points[0],points[1])
  m2,c2 = get_line(points[1],points[2])
  m3,c3 = get_line(points[2],points[0])

  a = x*m1 + y*(-1) + c1
  b = x*m2 + y*(-1) + c2
  c = x*m3 + y*(-1) + c3

  check = [a,-b,-c]
  for val in check:
    if (val >= 0):
      count +=1
  if (count == 3):
    i += 1

  count1 = 0
  m11,c11 = get_line(points[0],points[2])
  m22,c22 = get_line(points[2],points[3])
  m33,c33 = get_line(points[3],points[0])

  aa = x*m11 + y*(-1) + c11
  bb = x*m22 + y*(-1) + c22
  cc = x*m33 + y*(-1) + c33

  check1 = [-aa,-bb,cc]
  for vall in check1:
    if(vall <= 0):
      count1+=1
  if (count1 == 3):
    i += 1
  if (i == 0):
    return None
  else:
    return True

def check_for_obstacle_2(points,point):
  count = 0
  x,y = point[0],point[1]
  # m1,c1 = get_line(points[0],points[1]) // This doesn't work since division by zero is impossible.
  m2,c2 = get_line(points[1],points[2])
  m3,c3 = get_line(points[2],points[3])
  # m4,c4 = get_line(points[3],points[4]) // This doesn't work since division by zero is impossible.
  m5,c5 = get_line(points[4],points[5])
  m6,c6 = get_line(points[5],points[0])
  
  a = x - 165
  b = x*m2 + y*(-1) + c2
  c = x*m3 + y*(-1) + c3
  d = x - 235
  e = x*m5 + y*(-1) + c5
  f = x*m6 + y*(-1) + c6

  check = [a,b,c,-d,-e,-f]
  for val in check:
    if (val >= 0):
      count += 1
  if (count == 6):
    return True
  else:
    return None

def check_for_obstacle_3(point):
  x,y = point[0],point[1]
  a = ((x-300)**2) + ((y-185)**2) - (40*40)
  if (a <= 0):
    return True
  else:
    return None

def get_obstacle_coord(obstacle_1,obstacle_2):

  obs_coord_list=[]
  mat = np.ones((400,250,3))
  for x in range(0,400):
    for y in range (0,250):
      point = [x,y]
      if (check_for_obstacle_1(obstacle_1,point)) or (check_for_obstacle_2(obstacle_2,point)) or (check_for_obstacle_3(point)):
        obs_coord_list.append([x,y])
        mat[x][y] = (0,0,0)
  image = cv2.rotate(mat, cv2.ROTATE_90_COUNTERCLOCKWISE)
  cv2.imshow('asd',image)
  cv2.waitKey(0)
  return obs_coord_list

if __name__ == '__main__':

  obstacle_1 = [[36,185],[115,210],[80,180],[105,100]]
  obstacle_2 = [[165,82.5],[165,117.5],[200,139.13],[235,117.5],[235,82.5],[200,60.87]]
  obstacles = get_obstacle_coord(obstacle_1,obstacle_2)
