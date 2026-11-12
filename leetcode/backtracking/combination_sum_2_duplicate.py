def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    result = list()
    candidates.sort()
    # candidates are sorted to begin with
    # so that the rest of the candidates
    # can be rejected at the first non-valid
    # candidate
    candict = dict()
    used = dict()
    for candidate in candidates:
        if candidate not in candict:
            candict[candidate] = 0
            used[candidate] = 0
        candict[candidate] += 1

    keys = list(candict.keys())

    def backtrack(i, sum, res):
        if sum == target:
            result.append(res[:])
            return
        for k in range(i, len(candidates)):
            if sum + candidates[k] > target:
                break   # continue will check the rest of the candidate
            if k > i and candidates[k] == candidates[k-1]:  # skip the duplicate need to understand the k > 1 condition
                continue
            
            res.append(candidates[k])
            backtrack(k+1, sum + candidates[k], res)
            res.pop()

    backtrack(0, 0, [])
    return result


if __name__=="__main__":
    print(combinationSum2([10,1,2,7,6,1,5], 8))