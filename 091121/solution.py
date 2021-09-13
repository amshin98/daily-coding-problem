def level_wise(root):
   queue = []
   queue.append(root)

   ans = []

   while queue:
      cur_node = queue.pop(0)
      ans.append(str(cur_node.data))

      if cur_node.left:
         queue.append(cur_node.left)
      if cur_node.right:
         queue.append(cur_node.right)

   print(ans)