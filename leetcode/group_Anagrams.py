class Solution:
    def groupAnagrams(self, strs) :
        dic = {}
        for item in strs:
            key = ''.join(sorted(item))
            if key in dic:
                dic[key].append(item)
            else:
                dic[key] = [item]
        return list(dic.values())

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))