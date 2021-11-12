import sys 
def mult_div_and_conq(a, b, c):
    if b == 1:
        return a % c
    answer = mult_div_and_conq(a, b//2, c)
    if b % 2 == 1:
        return (a * answer * answer) % c
    else:
        return (answer * answer) % c


if __name__ == '__main__':
    input = sys.stdin.readline
    a, b, c = map(int, input().split())
    print(mult_div_and_conq(a, b, c))