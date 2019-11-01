import collections
class Solution:
    def reconstructQueue(self, people):
        res = []
        pdic = collections.defaultdict(list)
        for i, p in enumerate(people):
            pdic[p[0]] += [(p[1], i)]
        height = sorted(pdic.keys())
        for h in height[::-1]:
            pdic[h].sort()
            for p in pdic[h]:
                res.insert(p[0],people[p[1]])
        return res
        
a = Solution()
print(a.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))