def subsets(nums: list[int]) -> list[list[int]]:
    result = list()

    def backtrack(i, res):
        # understand what i is and isn't
        if len(nums) == i:
            result.append(res[:])
            return
        
        res.append(nums[i])
        backtrack(i+1, res)

        res.pop()
        # here not choosing a branch
        # itself adds a level of 
        # recursion depth
        backtrack(i+1, res)

    backtrack(0, [])
    return result

if __name__=="__main__":
    print(subsets([1, 2, 3]))