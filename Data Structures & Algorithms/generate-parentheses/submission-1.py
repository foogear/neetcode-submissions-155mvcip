class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def placeBrackets(totalCell):
            if totalCell  < 2:
                return ['']
            if totalCell == 2:
                return ['()']

            L, R = 0, -1
            res = []
            # while R < totalCell: NEVER do this
            while R + 2 < totalCell:
                R += 2 # just make sure L = 1, 3, 5...

                # build Left  (? ?)_ _
                leftParts = placeBrackets(R - L - 1)
                for i in range(len(leftParts)):
                    leftParts[i] = '(' + leftParts[i] + ')'

                # build right (_ _)? ?
                rightParts = placeBrackets(totalCell - R - 1)

                for left in leftParts:
                    for right in rightParts:
                        res.append(left + right)

            return res
            
        return placeBrackets(n * 2)