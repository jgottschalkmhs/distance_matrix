points = ["A", "B", "C", "D"]

# Loop generates correct number of points pairs.
count = 0
while count < len(points) - 1: 
  count2 = count + 1
  while count2 < len(points):
    # calculation / call to function would go here
    print(points[count] + points[count2])
    count2 += 1
  count += 1