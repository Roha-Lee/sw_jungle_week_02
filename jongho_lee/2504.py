import sys 
def is_valid_parenthesis(parenthesis):
    stack = []
    pair_dict = {')':'(', ']':'['}
    for letter in parenthesis:
        if letter == '(' or letter == '[':
            stack.append(letter)
        elif letter == ')' or letter == ']':
            if stack and stack[-1] == pair_dict[letter]:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


def get_parenthesis_value(parenthesis):
    if not is_valid_parenthesis(parenthesis):
        return 0
    digit_convert = {'(': 2, '[' : 3}
    parenthesis.reverse()
    stack = []
    
    while parenthesis:
        curr = parenthesis.pop()
        if curr == '(' or curr == '[':
            stack.append(curr)
        elif curr == ')' or curr == ']':
            results = 0        
            while type(stack[-1]) == type(0):
                results += stack.pop()
            results = 1 if results == 0 else results
            results *= digit_convert[stack.pop()]
            stack.append(results)
            
    return sum(stack)


if __name__ == '__main__':
    input = sys.stdin.readline
    parenthesis = list(input().rstrip())
    print(get_parenthesis_value(parenthesis))