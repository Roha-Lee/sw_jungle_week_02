import sys 
def make_max_num(number_list, k):
    remain = k
    result = []
    for i in range(len(number_list)):
        while result and remain and result[-1] < number_list[i]:
            result.pop()
            remain -= 1
        result.append(number_list[i])
    return ''.join([str(num) for num in result[:len(number_list)-k]])


if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = map(int, input().split())
    number = list(map(int, input().rstrip()))
    print(make_max_num(number, k))
    