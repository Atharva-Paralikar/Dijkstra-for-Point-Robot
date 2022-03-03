## License
```
MIT License

Copyright (c) 2022 Atharva Paralikar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Overview of Dijkstra Algorithm

Dijkstra's algorithm is an algorithm for finding the shortest path between nodes in a graph. Here we modify it to find the optimal path based on the cost of each action taken by a point robot. we try to minimize this cost.

The Psuedo-code for Dijkstra algorithm:

![Psuedo-code](https://github.com/Atharva-Paralikar/Dijkstra-for-Point-Robot/blob/main/docs/psuedo_code_dijkstra.png)

The action cost for the path is:

![Action-set and costs](https://github.com/Atharva-Paralikar/Dijkstra-for-Point-Robot/blob/main/docs/action_cost.png)

## Steps to Run Code

1. Copy the repository
```
git clone --recursive https://github.com/Atharva-Paralikar/Dijkstra-for-Point-Robot
```
2. Source the repository 
```
cd ~/Dijkstra-for-Point-Robot
```
3. Run the package 
```
python3 dijkstra.py
```
## Obstacle Map

![Obstacle Map](https://github.com/Atharva-Paralikar/Dijkstra-for-Point-Robot/blob/main/docs/obstacle_map.jpg)

## Visualisation of the Node Exploration

Start Node = [150,200]

Goal Node = [300,80]

![Node Exploration](https://github.com/Atharva-Paralikar/Dijkstra-for-Point-Robot/blob/main/docs/exploration.gif)

## Optimal Path Generation

Start Node = [150,200]

Goal Node = [300,80]

![Optimal Path](https://github.com/Atharva-Paralikar/Dijkstra-for-Point-Robot/blob/main/docs/path.jpg)
