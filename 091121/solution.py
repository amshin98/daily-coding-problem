def level_wise(root):
   queue = []
   queue.append(root)

   while queue:
      cur_node = queue.pop(0)
      print(cur_node.data)

      if cur_node.left:
         queue.append(cur_node.left)
      if cur_node.right:
         queue.append(cur_node.right)