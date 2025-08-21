from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([f'{len(word)}#' + word for word in strs])

    def decode(self, s: str) -> List[str]:
        i = 0
        _storage = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            _storage.append(s[start:end])
            i = end
        return _storage

if __name__ == '__main__':
    s = Solution()
    print(s.encode("abc"))
    print(s.decode("abc"))
