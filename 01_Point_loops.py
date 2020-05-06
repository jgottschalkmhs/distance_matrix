points = ["A", "B", "C", "D"]

combined = []

# loop pairs all points
count = 0

for item in points:
  for item in points:
    code = points[count]+item
    combined.append(code)
  count+=1

combined.sort()

for item in combined:
  print(item)

