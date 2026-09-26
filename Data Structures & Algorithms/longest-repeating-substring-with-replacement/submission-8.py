class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # We can have a hashmap for each word that is within our window. 
        # This hashmap will count how many times each letter is there. 
        # We can simply get the max of that hashmap to get the letter that is in the window the most times. 
        # We can do r+l-1 - max(seen) to get the amount of k that we can do. If it is under k, then we have a valid window that we can check with max(res, r+l-1)

        # Now that we know the mechanism, let us think about how we will iterate.
        # Change what we did before. Let us use k as an indicator as to whether we should continue iterating r or iterate some of l. 
        # If the number of letters that can be changed to keep the window valid is < k, then we continue with r. Once > k, we iterate l.

        l = 0 
        res = 0 
        seen = defaultdict(int)

        for r, c in enumerate(s) : 
            seen[s[r]] += 1 
            while len(seen) > 0 and ((r-l+1) - max(seen.values())) > k : 
                seen[s[l]] -= 1 
                l+=1 
            res = max(res, r-l+1)
        return res 