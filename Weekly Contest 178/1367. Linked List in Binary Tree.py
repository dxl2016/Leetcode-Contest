# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False
            
            if head.val == root.val:
                return dfs(head.next, root.left) or dfs(head.next, root.right)
            else:
                return False
        
        if not root:
            return False 
        if head.val == root.val and dfs(head, root):
            return True
        else:
            return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

