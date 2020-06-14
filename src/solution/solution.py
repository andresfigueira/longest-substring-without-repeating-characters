def solution(s: str) -> int:
    longest = l = 0
    used = {}

    for r, c in enumerate(s):
        if c in used and l <= used[c]:
            l = used[c] + 1
        else:
            longest = max(longest, r - l + 1)

        used[c] = r

    return longest
