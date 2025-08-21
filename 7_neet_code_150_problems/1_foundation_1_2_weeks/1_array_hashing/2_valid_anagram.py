import time


def isAnagram(s: str, t: str) -> bool:
    result = sorted(s) == sorted(t)
    return result


# Example usage
print(isAnagram("listen", "silent"))
