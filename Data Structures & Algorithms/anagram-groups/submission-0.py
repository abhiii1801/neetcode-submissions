class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}
        
        for s in strs:
            ss = sorted(s)
            if tuple(ss) in hmap:
                hmap[tuple(ss)].append(s)
            else:
                hmap[tuple(ss)] = [s]

        return list(hmap.values())
            