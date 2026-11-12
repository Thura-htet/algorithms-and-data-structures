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
        """
        for k in range(i, n):
            if sum + candidates[k] > target:
                break   # continue will check the rest of the candidate
            if candidates[k] == candidates[k-1]:
                continue
            
            sum += candidates[k]
            res.append(candidates[k])
            backtrack(k+1, sum, res)
            res.pop()
            sum -= candidates[k]
        """
        """
        for k, (candidate, count) in enumerate(candict.items()):
            if k < i:   # this is what produces the staggering effect 
                continue
            if sum + candidate > target:
                break       # exit the loop entire
            if used[candidate] >= count:
                continue    # move on to the next candidate but i doesn't reset

            # for the moment i doesn't represent the count for indiviual candidate
            res.append(candidate)
            used[candidate] += 1
            backtrack(k+1, sum + candidate, res)
            res.pop()
            used[candidate] -= 1
        """
        for k in range(i, len(keys)):
            candidate = keys[k]

            if sum + candidate > target:
                break
            if used[candidate] >= candict[candidate]:
                continue

            res.append(candidate)
            used[candidate] += 1
            backtrack(k, sum + candidate, res)
            res.pop()
            used[candidate] -= 1

    backtrack(0, 0, [])
    return result


if __name__=="__main__":
    print(combinationSum2(
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        , 30))