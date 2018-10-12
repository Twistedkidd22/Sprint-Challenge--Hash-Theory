def reconstruct_trip(tickets):
  ht = {}

  route = []

  for t in tickets:
    ht[t[0]] = t[1]

 
  current = ht[None]

  route.append(current)

  next = ht[None] 

  while (next != None):
    try:
      next = ht[next]
      
      if (next):
        route.append(next)
    except:
      return []
  
  return route




if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  tickets = [
    ('PIT', 'ORD'),
    ('XNA', 'CID'),
    ('SFO', 'BHM'),
    ('FLG', 'XNA'),
    (None, 'LAX'), 
    ('LAX', 'SFO'),
    ('CID', 'SLC'),
    ('ORD', None),
    ('SLC', 'PIT'),
    ('BHM', 'FLG'),
  ]
  print (reconstruct_trip(tickets))
  pass
