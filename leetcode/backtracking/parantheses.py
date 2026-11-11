def generateParenthesis(n: int) -> list[str]:
    result = list()
    choices = ["(", ")"]

    def backtrack(opened, closed, res):
        if len(res)==2*n:
            result.append(res)
            return
        # the index that is being passed in as a parameter
        # never decides the number of for loop iterations
        """ 
        for k in range(n-i):
            res += "("
            backtrack(i+1, res)
            res += ")"
            backtrack(i+1, res)
        print(res)
        """
        for choice in choices:
            before = res
            if choice == "(":
                if opened < n:
                    res += choice
                    backtrack(opened+1, closed, res)
            else:
                if closed < opened:
                    res += choice
                    backtrack(opened, closed+1, res)
            res = before
    backtrack(0, 0, "")        
    return result

if __name__=="__main__":
    print(generateParenthesis(4))