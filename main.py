
class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None
        self.status = False
    
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)

    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRootVal(self):
        return self.key

    def isVisited(self):
        return self.status

    def setVisited(self):
        self.status = True

class KDTree:
    
    
    def __init__(self, obstacle_list):
        self.obstacle_list = obstacle_list
        self.rootNode = None
        l, n, r = self.seperate_list(self.obstacle_list)
        self.rootNode = BinaryTree(n)
        self.addNode(self.rootNode, l, r)

    def addNode(self, rootNode, leftList, rightList):
        if(len(leftList) > 0):
            l, n, r = self.seperate_list(leftList)
            rootNode.insertLeft(n)
            self.addNode(rootNode.getLeftChild(), l, r)
        if(len(rightList) > 0):
            l, n, r = self.seperate_list(rightList)
            rootNode.insertRight(n)
            self.addNode(rootNode.getRightChild(), l, r)
    
    def getRootNode(self):
        return self.rootNode

    def seperate_list(self, source_list):
        if len(source_list) == 1:
            return [], (source_list[0][0], source_list[0][1], 0), []
        x_axis = 0
        y_axis = 0
        for coord in source_list:
            x_axis += int(coord[0])
            y_axis += int(coord[1])
        x_list = [coord[0] for coord in source_list]
        y_list = [coord[1] for coord in source_list]
        x_avg = x_axis / len(source_list)
        y_avg = y_axis / len(source_list)
        x_varanice = self.compute_varanice(x_avg, x_list)
        y_varanice = self.compute_varanice(y_avg, y_list)
        if x_varanice > y_varanice:
            # seperate on x
            result_list = sorted(source_list, key=lambda x:x[0])
            axis = 0
        else:
            # seperate on y
            result_list = sorted(source_list, key=lambda x:x[1])
            axis = 1
        left_list = result_list[0:int(len(result_list)/2)]
        right_list = result_list[int(len(result_list)/2)+1:]
        node = result_list[int(len(result_list)/2)]
        #node in tuple format
        return left_list, (node[0], node[1], axis), right_list

    def compute_varanice(self, avg, coord_list):
        variance = 0
        for l in coord_list:
            variance += (l-avg) ** 2
        return variance / len(coord_list)
        
def dis(coord1, coord2):
    return ((coord1[0]-coord2[0])**2+(coord1[1]-coord2[1])**2)**0.5

def DFS(root, path):
    while root != None:
        coord = root.getRootVal()
        axis = coord[2]
        path.append(root)
        root.setVisited()
        if axis == 0:
            if target[0] <= coord[0]:
                root = root.getLeftChild()
            else:
                root = root.getRightChild()
        else:
            if target[1] <= coord[1]:
                root = root.getLeftChild()
            else:
                root = root.getRightChild()
    return path

if __name__ == "__main__":
    K = 3
    target = (2, 4.5)
    obstacle_list = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
    kdtree = KDTree(obstacle_list)
    path = []
    topk = []
    root = kdtree.getRootNode()
    while root!=None:
        coord = root.getRootVal()
        axis = coord[2]
        path.append(root)
        root.setVisited()
        if axis == 0:
            if target[0] <= coord[0]:
                root = root.getLeftChild()
            else:
                root = root.getRightChild()
        else:
            if target[1] <= coord[1]:
                root = root.getLeftChild()
            else:
                root = root.getRightChild()
    for p in path:
        print(p.getRootVal())
    # compute leaf node
    p = path.pop()
    topk.append(dis(target, p.getRootVal()))
    while len(path)>0:
        print("------start-------")
        for p in path:
            print(p.getRootVal())
        print("------end-------")
        print(topk)
        p = path.pop()
      
        if len(topk) < K:
            topk.append(dis(target, p.getRootVal()))
            topk.sort()
            root = p
            if root.getLeftChild() != None and not root.getLeftChild().isVisited():
                path = DFS(root.getLeftChild(), path)
            elif root.getRightChild() != None and not root.getRightChild().isVisited():
                path = DFS(root.getRightChild(), path)
        else:
            temp = topk[len(topk)-1]
            coord = p.getRootVal()
            print(coord)
            print(str(coord) +"dis to target is"+str(dis(target, coord)))
            if dis(target, coord) < temp:
                    topk.pop()
                    topk.append(dis(target, coord))
                    topk.sort()

            if coord[2] == 0:
                dis_to_line = abs(target[0]-coord[0])
            else:
                dis_to_line = abs(target[1]-coord[1])
            if dis_to_line < temp:
                # find the other branch
                root = p
                if root.getLeftChild() != None and not root.getLeftChild().isVisited():
                    path = DFS(root.getLeftChild(), path)
                elif root.getRightChild() != None and not root.getRightChild().isVisited():
                    path = DFS(root.getRightChild(), path)
    print(topk)



            

        
    
        
    

    