def findPoint(px, py, qx, qy):

    # Write your code here
    rx = 2 * qx - px
    ry = 2 * qy - py
    return [rx, ry]
n = int(input().strip())
for _ in range(n):
        px, py, qx, qy = map(int, input().split())
        reflection = findPoint(px, py, qx, qy)
        print(*reflection)
