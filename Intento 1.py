import numpy as np
b = np.random.randint(18,65,(365,20)) 
c = np.random.randint(1234567893,9876543287,(365,20))
out = []
inn = []
for i in range(365):
  for j in range(20):
    numero = b[i,j]
    if numero >= 40:

      out.append((i,j))

      cel = c[i,j]
      inn.append((cel))
      
