# K-Nearest-Neighbour
Use KD Tree method to find K nearest value to specific coorinate on 2D Plane

## Setup
Run with command:
```
python main.py
```

## Structure
```
├── Readme.md                   // help  
├── main.py  
│   ├── class BinaryTree
│   │   ├── __init__()  
│   │   ├── insertLeft()  
│   │   └── insertRight()  
│   │   └── isVisited()  
│   ├── class KD Tree
│   │   ├── __init__()  
│   │   ├── addNode()  
│   │   └── seperateList()  
│   ├── main()
```

## Method
* Construct KD Tree:
```
*   Find the medium value on the dimension with bigger varanice and take it as root node
*   Seperate the list into left list and right list and resolve them reversely
*   Left child node means all the points are to the left (on that dimension) of the node, right child node is same way
![image](https://github.com/Wan-woo/KNearestNeighbout/blob/main/IMG/KD%20tree.png)
```
* Find the nearest K neighbour in KD Tree
```
*   Start from root, and compare with each node to decide left or right till leaf
*   Reverse to compare: 
    If there exists closer distance on the other branch of the parent node, add it to path (If circle intersects with line)
    If the distance from target to parent is closer than the biggest element of TopK array, update and sort it; If TopK has less than K elements, simply add it to TopK
    Path is empty, everything is done
```
Something to mention: we use TopK to trace K nearest, when K = 1, it means cloest

## Input
```
K = 3
target = (2, 4.5)
obstacle_list = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
```

## Output
```
[1.5, 3.0413812651491097, 3.2015621187164243]
```