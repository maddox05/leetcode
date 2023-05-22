class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for i in strs[1:]:
            if not prefix:
                return prefix

            while not i.startswith(prefix):
                prefix = prefix[:-1]
        return prefix
