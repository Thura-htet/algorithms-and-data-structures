def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    result = list()
    n = len(candidates)
    candidates.sort()
    # candidates are sorted to begin with
    # so that the rest of the candidates
    # can be rejected at the first non-valid
    # candidate

    def backtrack(i, sum, res):
        if sum == target:
            result.append(res[:])
            return

        for k in range(i, n):
            if sum + candidates[k] > target:
                break   # continue will check the rest of the candidate
            sum += candidates[k]
            res.append(candidates[k])
            backtrack(k, sum, res)
            res.pop()
            sum -= candidates[k]

    backtrack(0, 0, [])
    return result


if __name__=="__main__":
    print(combinationSum([2,3,5], 8))