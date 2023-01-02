with open('input.txt') as f:
  data = f.read().splitlines()

# Determine size of forest
height = len(data)
width = len(data[0])
perim = height*2 + width*2 - 4

# Create forest as nested list
forest = []
for line in data:
  row = []
  for tree in line:
    row.append(int(tree))
  forest.append(row)

# Part 1 variables
visibler = []
visiblel = []
visibleu = []
visibled = []

# Part 2 variables
distancer = []
distancel = []
distanceu = []
distanced = []

# Get each tree in turn not looking at edge trees
for r in range(1,width-1):
  for c in range(1,height-1):
    
    # Look right
    vis = 1
    count = 0
    i = c+1
    while i < width:
      count += 1
      if forest[r][c] <= forest[r][i]:
        vis = 0
        break
      i += 1
    visibler.append(vis)
    distancer.append(count)
    
    # Look down
    vis = 1
    count = 0
    i = r+1
    while i < height:
      count += 1
      if forest[r][c] <= forest[i][c]:
        vis = 0
        break
      i += 1
    visibled.append(vis)
    distanced.append(count)

    # Look left
    vis = 1
    count = 0
    i = c-1
    while i >= 0:
      count += 1
      if forest[r][c] <= forest[r][i]:
        vis = 0
        break
      i -= 1
    visiblel.append(vis)
    distancel.append(count)

    # Look up
    vis = 1
    count = 0
    i = r-1
    while i >= 0:
      count += 1
      if forest[r][c] <= forest[i][c]:
        vis = 0
        break
      i -= 1
    visibleu.append(vis)
    distanceu.append(count)

# Part 1
tot_vis = []
for x in range(len(visibler)):
  tot_vis_direction = visibler[x]+visiblel[x]+visibleu[x]+visibled[x]
  if tot_vis_direction > 0:
    tot_vis.append(1)

# Sum of visible inner trees plus all trees around edge
print("Part 1:", sum(tot_vis) + perim)

# Part 2
score = []

for y in range(len(distancer)):
  tot_dist = distancer[y]*distancel[y]*distanceu[y]*distanced[y]
  score.append(tot_dist)

# Maximum visibility score
print("Part 2:", max(score))