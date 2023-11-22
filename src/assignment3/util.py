def runner_up_score(value):
    arr = map(int, input().split())
    remove_duplicate=list(set(arr))
    remove_duplicate.sort()
    print(remove_duplicate[-2])

