import collections 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #3 arrays -- one is visited, other is just for the queue, and the other is level by level 


        visited = [] #first array

        #second array
        q = collections.deque() #just a handy library tool
        q.append(root)

        # so long as there are nodes
        while q:
            #3rd array for level
            level = []

            for i in range(len(q)):
                #pop(0) & returned
                node_popped = q.popleft()

                #now check if we indeed popped a node
                if node_popped:
                    #append to level (as visited), and put its children in the queue
                    level.append(node_popped.val) #extract val
                    q.append(node_popped.left)
                    q.append(node_popped.right)
                
            #after looping through, if level has something
            if level:
                visited.append(level) #append the visited of level arr, into visited (lists of list)
        
        return visited







                

            

