class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score1 = sorted(score,reverse=True)
        ans = []
        for i in range(len(score)):
            if score[i] == score1[0]:
                ans.append("Gold Medal")
            elif score[i] == score1[1]:
                ans.append("Silver Medal")
            elif score[i] == score1[2]:
                ans.append("Bronze Medal")
            else:    
                ans.append(str(score1.index(score[i]) + 1))
        return ans