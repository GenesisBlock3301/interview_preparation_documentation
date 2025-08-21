from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hash_map = dict()
    for word in strs:
        key = ''.join(sorted(word))
        if key in hash_map:
            hash_map[key].append(word)
        else:
            hash_map[key] = [word]
    return list(hash_map.values())


strs = ["act","pots","tops","cat","stop","hat"]

print(groupAnagrams(strs))