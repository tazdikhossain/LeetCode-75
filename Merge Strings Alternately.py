class Solution:
    def mergeAlternately(self, word1, word2):
        result = ""
        n = len(word1)
        m = len(word2)

        for i in range(min(n, m)):
            result += word1[i]
            result += word2[i]

        if n > m:
            result += word1[m:]
        else:
            result += word2[n:]

        return result
