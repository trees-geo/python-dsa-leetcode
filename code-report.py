class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store=dict()
        max_length=0
        left=0
        for right in range(len(s)):
            print(right)
            print(store)
            print(left)
            print('***************************')
            if s[right] in store:
                store[s[right]] +=1
                while store.get(s[right]) >2:
                    store[s[left]] -=1
                    left+=1
            else:
                store[s[right]] =1
            max_length = max(max_length, right-left+1)
        return max_length

s = Solution()
print(s.lengthOfLongestSubstring('ecebae'))
# Length of longest unique substring with atmost 2 repetitions of character
