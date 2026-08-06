class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = 0
        fixed = Counter(s1)
        hmap = defaultdict(int)

        for r in range(len(s2)):
            hmap[s2[r]] += 1

            if r >= len(s1):
                hmap[s2[r - len(s1)]] -= 1

                if hmap[s2[r - len(s1)]] == 0:
                    del hmap[s2[r - len(s1)]]

            if fixed == hmap:
                return True

        return False




