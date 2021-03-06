import numpy as np
import cv2
import math

class Node:
  def __init__(self,data,parent,cost):
    self.Node_state = data
    self.Node_parent_node = parent
    self.Node_cost_to_reach = cost

def get_line(A,B):
  x1,y1,x2,y2 = A[0],A[1],B[0],B[1]
  m = (y2-y1)/(x2-x1)
  c = y1 - m * x1
  return m,c

def check_for_obstacle_1(points,point): ## returns if the coordinate is within quadrilateral obstacle
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
      count1 += 1
  if (count1 == 3):
    i += 1
  if (i == 0):
    return None
  else:
    return True

def check_for_obstacle_2(points,point):   ## returns if the coordinate is within hexagonal obstacle
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

def check_for_obstacle_3(point):    ## returns if the coordinate is within circular obstacle
  x,y = point[0],point[1]
  a = ((x-300)**2) + ((y-185)**2) - (40*40)
  if (a <= 0):
    return True
  else:
    return None

def get_obstacle_coord(obstacle_1,obstacle_2):

  obs_coord_list=[]
  mat_img = np.ones((401,251,3))
  mat = np.ones((406,256))
  for x in range(0,400):
    for y in range (0,251):
      point = [x,y]
      if (check_for_obstacle_1(obstacle_1,point)) or (check_for_obstacle_2(obstacle_2,point)) or (check_for_obstacle_3(point)):
        obs_coord_list.append([x,y])
        mat_img[x][y] = (0,0,0)
        mat[x][y] = 0

  return obs_coord_list,mat_img,mat

  ############## Action Sets ##################

def action_Up(curr_node,matrix):

  x,y = curr_node.Node_state[0],curr_node.Node_state[1]

  if y < 249:
    x_new = x
    y_new = y + 1
    cost = curr_node.Node_cost_to_reach + 1
    if matrix[x_new][y_new + 5] == 1 and matrix[x_new + 5][y_new + 5] == 1 and matrix[x_new - 5][y_new + 5]:
      newNode = Node([x_new,y_new],curr_node,cost)
      return newNode
    else:
      # print("Obstacle found at: ",x_new,y_new)
      return False
  else:
    return False

def action_Down(curr_node,matrix):

  x,y = curr_node.Node_state[0],curr_node.Node_state[1]
  if y > 0:
    x_new = x
    y_new = y - 1
    cost = curr_node.Node_cost_to_reach + 1
    if matrix[x_new][y_new - 5] == 1 and matrix[x_new + 5][y_new - 5] == 1 and matrix[x_new - 5][y_new - 5]:
      newNode = Node([x_new,y_new],curr_node,cost)
      return newNode
    else:
      # print("Obstacle found at: ",x_new,y_new)
      return False
  else:
    return False

def action_Right(curr_node,matrix):

  x,y = curr_node.Node_state[0],curr_node.Node_state[1]
  if x < 400:
    x_new = x + 1
    y_new = y
    cost = curr_node.Node_cost_to_reach + 1
    if matrix[x_new + 5][y_new] == 1 and matrix[x_new + 5][y_new - 5] == 1 and matrix[x_new + 5][y_new + 5]:
      newNode = Node([x_new,y_new],curr_node,cost)
      return newNode
    else:
      # print("Obstacle found at: ",x_new,y_new)
      return False
  else:
    return False

def action_Left(curr_node,matrix):

  x,y = curr_node.Node_state[0],curr_node.Node_state[1]
  if x > 0:
    x_new = x - 1
    y_new = y
    cost = curr_node.Node_cost_to_reach + 1
    if matrix[x_new - 5][y_new] == 1 and matrix[x_new - 5][y_new - 5] == 1 and matrix[x_new - 5][y_new + 5]:
      newNode = Node([x_new,y_new],curr_node,cost)
      return newNode
    else:
      # print("Obstacle found at: ",x_new,y_new)
      return False
  else:
    return False

def action_Up_Right(curr_node,matrix):

  x,y = curr_node.Node_state[0],curr_node.Node_state[1]
  if (x < 400) and (y < 250):
    x_new = x + 1
    y_new = y + 1
    cost = curr_node.Node_cost_to_reach + 1.4
    if matrix[x_new + 5][y_new + 5] == 1 and matrix[x_new][y_new + 5] == 1 and matrix[x_new + 5][y_new]:
      newNode = Node([x_new,y_new],curr_node,cost)
      return newNode
    else:
      # print("Obstacle found at: ",x_new,y_new)
      return False
  else:
    return False

def action_Up_Left(curr_node,matrix):

  x,y = curr_node.Node_state[0],curr_node.Node_state[1]
  if (x > 0) and (y < 250) :
    x_new = x - 1
    y_new = y + 1
    cost = curr_node.Node_cost_to_reach + 1.4
    if matrix[x_new - 5][y_new + 5] == 1 and matrix[x_new][y_new + 5] == 1 and matrix[x_new - 5][y_new]:
      newNode = Node([x_new,y_new],curr_node,cost)
      return newNode
    else:
      # print("Obstacle found at: ",x_new,y_new)
      return False
  else:
    return False

def action_Down_Right(curr_node,matrix):

  x,y = curr_node.Node_state[0],curr_node.Node_state[1]
  if (x < 400) and (y > 0):
    x_new = x + 1
    y_new = y - 1
    cost = curr_node.Node_cost_to_reach + 1.4
    if matrix[x_new + 5][y_new - 5] == 1 and matrix[x_new][y_new - 5] == 1 and matrix[x_new + 5][y_new]:
      newNode = Node([x_new,y_new],curr_node,cost)
      return newNode
    else:
      # print("Obstacle found at: ",x_new,y_new)
      return False
  else:
    return False

def action_Down_Left(curr_node,matrix):

  x,y = curr_node.Node_state[0],curr_node.Node_state[1]
  if (x > 0) and (y > 0):
    x_new = x - 1
    y_new = y - 1
    cost = curr_node.Node_cost_to_reach + 1.4
    if matrix[x_new - 5][y_new - 5] == 1 and matrix[x_new][y_new - 5] == 1 and matrix[x_new - 5][y_new]:
      newNode = Node([x_new,y_new],curr_node,cost)
      return newNode
    else:
      # print("Obstacle found at: ",x_new,y_new)
      return False
  else:
    return False

def action(i,curr_node,matrix):
  
  if i == 5:
    New_Node = action_Up(curr_node,matrix)
    if New_Node:
      return New_Node
    else:
      return False
  elif i == 6:
    New_Node = action_Down(curr_node,matrix)
    if New_Node:
      return New_Node
    else:
      return False
  elif i == 7:
    New_Node = action_Right(curr_node,matrix)
    if New_Node:
      return New_Node
    else:
      return False
  elif i == 8:
    New_Node = action_Left(curr_node,matrix)
    if New_Node:
      return New_Node
    else:
      return False
  elif i == 1:
    New_Node = action_Up_Right(curr_node,matrix)
    if New_Node:
      return New_Node
    else:
      return False
  elif i == 2:
    New_Node = action_Up_Left(curr_node,matrix)
    if New_Node:
      return New_Node
    else:
      return False
  elif i == 3:
    New_Node = action_Down_Right(curr_node,matrix)
    if New_Node:
      return New_Node
    else:
      return False
  elif i == 4:
    New_Node = action_Down_Left(curr_node,matrix)
    if New_Node:
      return New_Node
    else:
      return False

def generate_path(node,matrix):     ## Bactracking function and generates the path
  path = []
  path = [node.Node_state]
  while node.Node_parent_node != None:
    node = node.Node_parent_node
    path.append(node.Node_state)
  path.reverse()
  for element in path:
    matrix[element[0]][element[1]]=(0,0,255)
  
  img = cv2.rotate(matrix,cv2.ROTATE_90_COUNTERCLOCKWISE)
  img = cv2.convertScaleAbs(img, alpha=(255.0))
  cv2.imshow("path",img)
  cv2.imwrite("./docs/path.jpg",img)
  cv2.waitKey(5000)
  cv2.destroyAllWindows()
  return img

def dijkstra(initial,goal,matrix,matrix_image):   ## Dijksrta Algorithm
  
  i1 = 0

  mat_img = matrix_image.copy()
  queue = []
  visited = []
  state = []
  cost = []
  startNode = Node(initial,None,0)
  queue.append(startNode)
  state.append(startNode.Node_state)
  cost.append(startNode.Node_cost_to_reach)

  while queue:
    minimum_cost = min(cost)
    k = cost.index(minimum_cost)

    curr_node = queue.pop(k)
    state.pop(k)
    cost.pop(k)
    visited.append(curr_node.Node_state)
    if curr_node.Node_state != goal:
      for i in range(1,9):
        new_node = action(i,curr_node,matrix)
        if new_node != False:
          if new_node.Node_state == goal:
            print("Goal Reached. Cost to reach :",new_node.Node_cost_to_reach)
            print("Saving Frames...")

            for element in visited:
              x,y = element[0],element[1]
              mat_img[x][y] = (0,255,255)

              image = cv2.rotate(mat_img.copy(),cv2.ROTATE_90_COUNTERCLOCKWISE)
              image = cv2.convertScaleAbs(image, alpha=(255.0))
              h,w,layers = image.shape
              size = (w,h)
              cv2.imwrite("./docs/Images/"+str(i1)+".jpg",image)
              i1 += 1
        
            cv2.imshow("exploration",image)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()

            print("Generating Video...")

            last_image = generate_path(new_node,mat_img)
            resized_image = cv2.resize(last_image,size)
            for j in range (0,1200):
              cv2.imwrite("./docs/Images/"+str(int(i1+j))+".jpg",resized_image)

            explore = cv2.VideoWriter("./docs/exploration.mp4",cv2.VideoWriter_fourcc(*'mp4v'),600,size)
            
            for k in range (0,i1+1200):
              imgaer = cv2.imread("./docs/Images/"+str(k)+".jpg")
              explore.write(imgaer)
            explore.release()
            return 0


          if new_node.Node_state not in visited:
            if new_node.Node_state in state:
              i = state.index(new_node.Node_state)
              if new_node.Node_cost_to_reach < queue[i].Node_cost_to_reach:
                queue[i].Node_parent_node = new_node.Node_parent_node
                queue[i].Node_cost_to_reach = new_node.Node_cost_to_reach
            else:
              queue.append(new_node)
              state.append(new_node.Node_state)
              cost.append(new_node.Node_cost_to_reach)
              
              print ("Current Point : ",new_node.Node_state)

if __name__ == '__main__':

  start_x = int(input("Enter start position X between (0,400): "))
  start_y = int(input("Enter start position Y between (0,250): "))
  goal_x = int(input("Enter Goal position X between (0,400): "))
  goal_y = int(input("Enter Goal position Y between (0,250): "))   

  start = [start_x,start_y]
  goal = [goal_x,goal_y]

  obstacle_1 = [[36,185],[115,210],[80,180],[105,100]]
  obstacle_2 = [[165,82.5],[165,117.5],[200,139.13],[235,117.5],[235,82.5],[200,60.87]]
  obstacles, matrix_image,matrix = get_obstacle_coord(obstacle_1,obstacle_2)
  # print(obstacles)
  image = cv2.rotate(np.array(matrix), cv2.ROTATE_90_COUNTERCLOCKWISE)
  image = cv2.convertScaleAbs(image, alpha=(255.0))
  cv2.imwrite("./docs/obstacle_map.jpg",image)
  cv2.imshow('Obstacle Map',image)
  cv2.waitKey(5000)
  cv2.destroyAllWindows()

  if goal not in obstacles:
    dijkstra(start,goal,matrix,matrix_image)
  else:
    print("Goal in obstacles and cannot be reached")