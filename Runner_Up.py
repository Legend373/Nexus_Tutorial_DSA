def runner_up(n,arr):
    unique_set=sorted(set(arr))
    return unique_set[-2]



if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result=runner_up(n,arr)
    print(result)