def letterCombinations(digits: str) -> list[str]:
        result = list()
        
        keys = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        """
        def backtrack(d, c, res):
            n = len(keys[digits][d])    # length of possible characters
            d = d + c // n
            c = c % n

            if len(res) == len(digits): # or if d is one less than len(digits)
                result.append(res)

            if d == len(digits):        # this is doubtful
                return

            digit = digits[d]           # dth element of the digit string
            char = keys[digit][c]       # cth element of the corresponding key

            # there is no choice of value therefore no additional for loop
            # unless in a for loop
            before = res
            res += char
            backtrack(d, c+1, res)
            backtrack(d, c+1, before)

        """
        def backtrack(i, res):
            if i >= len(digits):
                if len(res) == len(digits):
                    result.append(res)
                return
            
            """
            if len(res) == len(digits):
                result.append(res)
            """
            choices = keys[digits[i]]
            for choice in choices:
                # print(f"i: {i}\tchoices:{choices}\tchoice:{choice}")

                res += choice
                # print(f"res: {res}")
                # print(f"before: {before}\n")
                backtrack(i+1, res)
                res = res[:-1]
                # backtrack(i+1, res) # not sure if i have to recall backtrack

        backtrack(0, "")
        return result


if __name__== "__main__":
    result = letterCombinations("23")
    print(result)