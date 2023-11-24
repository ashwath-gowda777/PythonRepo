def runner_up_score(values):
    remove_duplicate = list(set(values))
    remove_duplicate.sort()
    return remove_duplicate[-2]
     

