def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    result = list()

    def backtrack(sum, res):
        if sum == target:
            sort_res = sorted(res)
            if sort_res not in result:
                # result.append((res.sort()[:]))
                result.append(sorted(sort_res))
                return

        for candidate in candidates:
            if sum + candidate <= target:    # is it a while loop here?
                sum += candidate
                res.append(candidate)
                backtrack(sum, res)
                res.pop()
                sum -= candidate

    backtrack(0, [])
    return result


if __name__=="__main__":
    print(combinationSum([2,3,5], 8))