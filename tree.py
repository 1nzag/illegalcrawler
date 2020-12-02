
class Node:
    def __init__(self, item):
        self.data = item
        self.ChildList = []
        self.depth = 0
        self.ChildNum = 0
        #ChildList = [Node 1, Node 2, ...]

    def Insert(self, ChildNode):
        self.ChildList.append(ChildNode)
        self.ChildNum += 1
        return self.ChildNum
    

    

class Tree:
    def __init__(self, RootNode):
        self.root = RootNode
    
    def FindDepthNode(self, TargetDepth, IndexDepth = 0, CurNode = None):
        if CurNode == None:
            CurNode = self.root
        result = []
        
        if IndexDepth < TargetDepth:
            for Child in CurNode.ChildList:
                result += self.FindDepthNode(TargetDepth, IndexDepth + 1, Child)
            return result
        
        elif IndexDepth == TargetDepth:
            for Child in CurNode.ChildList:
                result.append(Child)
            return result

    def FindItem(self, target, CurNode = None):
        if CurNode == None:
            CurNode = self.root
        if CurNode.data == target:
            return True
        
        else:
            if CurNode.ChildNum == 0:
                return False
            
            else:
                for Child in CurNode.ChildList:
                    if self.FindItem(target, Child) == True:
                        return True
                
                return False


        