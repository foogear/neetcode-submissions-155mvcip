class Solution:
    def generateParenthesis(self, n: int) -> List[str]:



        def placeBrackets(totalCell):
            if totalCell  < 2:
                return ['']
            if totalCell == 2:
                return ['()']

            L, R = 0, -1
            res = []
            # while R < totalCell:
            # never do this
            while R + 2 < totalCell:
                #++++++++print(f'while {R} < {totalCell}')
                R += 2 # just make sure L = 1, 3, 5...

                # build Left  (? ?)_ _
                #+++++++++++print(f'recur {R - L - 1}')
                leftParts = placeBrackets(R - L - 1)
                for i in range(len(leftParts)):
                    leftParts[i] = '(' + leftParts[i] + ')'
                #+++++++++++print(f'L={leftParts}')
                #++++++++++print('**********')

                # build right (_ _)? ?
                #++++++++++++print(f'recur {totalCell - R - 1}')
                rightParts = placeBrackets(totalCell - R - 1)
                #++++++++++++++++print(f'R={rightParts}')
                #++++++++++++++++print('**********')

                for left in leftParts:

                    for right in rightParts:

                        res.append(left + right)

                
                
            print(f'return={res}')
            return res







        return placeBrackets(n * 2)