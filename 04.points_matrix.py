
points = ["A", "B", "C", "D"]


# Generate matrix...
distance_matrix = []

for item in range(0, len(points)):
  matrix_line = []
  for item in range(0, len(points)):
    line = matrix_line.append("*")

  distance_matrix.append(matrix_line)

# Loop generates correct number of points pairs.
count = 0
while count < len(points) - 1: 
  count2 = count + 1
  while count2 < len(points):
    # calculation / call to function would go here
    distance_matrix[count][count2] = (points[count] + points[count2])

    count2 += 1
  count += 1

for item in distance_matrix:
  print(item)

