class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()

        splits=s.split()
        reverse=list(reversed(splits))
        gap=' '.join(reverse)

        return gap