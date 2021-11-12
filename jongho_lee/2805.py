import sys 
def get_trees(tree_heights, m):
    return sum([tree_height - m for tree_height in tree_heights if tree_height > m])
    
if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    tree_heights = list(map(int, input().split()))
    left, right = 0, max(tree_heights)
    best = 0
    while left <= right: 
        mid = (left + right) // 2
        val = get_trees(tree_heights, mid)
        if val < m: 
            right = mid - 1
        else:
            best = mid
            left = mid + 1
    print(best)