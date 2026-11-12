"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
"""
def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    result = list()
    nums.sort()

    def backtrack(i, res):
        # if (len(n) == i):
        if res not in result:   # figuring out the appending case is nuanced and important
            result.append(res[:])
        
        for k in range(i, len(nums)):
            res.append(nums[k])
            backtrack(k+1, res)
            res.pop()

    backtrack(0, [])    
    return result

if __name__=="__main__":
    print(subsetsWithDup([1,2,2]))