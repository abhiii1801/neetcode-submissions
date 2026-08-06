class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        tcount = Counter(t)

        window = defaultdict(int)

        have = 0
        need = len(tcount)

        minl = float("inf")
        mins = [-1,-1]

        for r in range(len(s)):
            curr = s[r]

            window[curr] += 1

            if curr in tcount and window[curr] == tcount[curr]:
                have += 1

            while have == need :
                if (r - l + 1) < minl:
                    minl = r -l + 1
                    mins = [l,r]

                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1

        return s[mins[0]:mins[1]+1] if minl != float('inf') else ""



            

