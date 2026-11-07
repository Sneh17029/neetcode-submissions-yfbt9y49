class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        m = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }
        res = []
        path = []
        def dfs(index):
            # base case
            if index == len(digits):
                res.append("".join(path))
                return
            
            letters = m[int(digits[index])]
            
            for ch in letters:
                path.append(ch)
                dfs(index + 1)
                path.pop()
        
        dfs(0)
        print(res)
        return res