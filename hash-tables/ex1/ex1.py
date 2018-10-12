def get_indices_of_item_weights(weights, limit):
  ht = {}
  
  if len(weights) == 1: 
    return ()
  
  if len(weights) == 2:
    if (weights[0] + weights[1] == limit):
        if weights[0] > weights[1]:
          return (0, 1)
        else:
          return (1, 0)

  for i, w in enumerate(weights):
    ht[w] = i

  for key in ht:
    try:
      keyTest = ht[limit-key]
      if (keyTest):
        return (ht[limit-key], ht[key])
    except KeyError: 
      print('searching...')
    
    


if __name__ == '__main__':
  print (get_indices_of_item_weights([2], 2))
  print (get_indices_of_item_weights([3, 4, 5], 9))
  print (get_indices_of_item_weights([10, 14, 15, 16], 30))
  print (get_indices_of_item_weights([10, 16, 15, 14], 30))
  pass 