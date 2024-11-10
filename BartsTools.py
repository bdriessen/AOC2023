
def flood_fill_dfs(img, x, y):
    # Base case: if the current pixel is not
    # the same as the previous color
    if img[x][y] != 0:
        return

    # Marking it as the new color
    img[x][y] = 1

    # Moving up, right, down, and left one by one
    n = len(img)
    m = len(img[0])
    if x - 1 >= 0:
        flood_fill_dfs(img, x - 1, y)
    if y + 1 < m:
        flood_fill_dfs(img, x, y + 1)
    if x + 1 < n:
        flood_fill_dfs(img, x + 1, y)
    if y - 1 >= 0:
        flood_fill_dfs(img, x, y - 1)


def flood_fill(image, x, y):
    # Create a copy of the image
    newimage = copy.deepcopy(image)
    # Create a queue and append the starting pixel
    queue = [(x, y)]
    # Get the color of the starting pixel
    color = 1
    # Get the number of rows and columns
    n = len(newimage)
    m = len(newimage[0])
    ic(n, m)
    # While the queue is not empty
    while queue:
        ic(queue)
        # Get the current pixel
        x, y = queue.pop(0)
        # If the current pixel is not the same as the starting pixel
        if newimage[x][y] == color:
            continue
        # Mark the current pixel as visited
        newimage[x][y] = 1
        # Append the neighbors of the current pixel
        if x - 1 >= 0:
            queue.append((x - 1, y))
        if y + 1 < m:
            queue.append((x, y + 1))
        if x + 1 < n:
            queue.append((x + 1, y))
        if y - 1 >= 0:
            queue.append((x, y - 1))
    # Return the modified image
    return newimage


def shoelace(trenches):
    n = len(trenches)
    ic(n)
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += trenches[i][0] * trenches[(i + 1) % n][1]
        sum2 += trenches[i][1] * trenches[(i + 1) % n][0]
    return abs(sum1 - sum2) / 2
