import random as rd

m = rd.sample(range(100), 15)

print("Yes" if sum(i for i in m if i % 2 != 0) > sum(i for i in m if i % 2 == 0)
      else "No")
