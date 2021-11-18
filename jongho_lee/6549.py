# 분할정복
import sys 

def get_area_from_center(histograms, mid):
    first = mid - 1
    second = mid
    min_height = min(histograms[first], histograms[second])
    width = 2
    max_area = min_height * width
    while not (first == 0 and second == len(histograms)-1):
        curr_height = 0 
        if first == 0:
            second += 1
            curr_height = histograms[second]
        elif second == len(histograms) - 1:
            first -= 1
            curr_height = histograms[first]
        elif histograms[first - 1] > histograms[second + 1]:
            first -= 1
            curr_height = histograms[first]
        else:
            second += 1
            curr_height = histograms[second]

        min_height = min(min_height, curr_height)
        width += 1
        max_area = max(max_area, min_height * width)
    return max_area    

def get_area(histograms):
    if len(histograms) == 1:
        return histograms[0]
    
    mid = len(histograms) // 2
    
    return max(
        get_area_from_center(histograms, mid), 
        get_area(histograms[:mid]),
        get_area(histograms[mid:])
    )

if __name__ == '__main__':
    input = sys.stdin.readline
    while True:
        usr_input = list(map(int, input().split()))    
        n = usr_input[0]
        if n == 0:
            break
        histograms = usr_input[1:]
        print(get_area(histograms))
