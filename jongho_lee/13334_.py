import sys 
def find_num_of_people_in_best_rail(rails, n, length):
    q = sorted(rails)
    

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    rails = []
    for _ in range(n):
        a, b = map(int(input()))
        rails.append( (min(a, b), max(a, b)) )
    length = map(int(input()))

