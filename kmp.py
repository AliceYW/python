def ff(pattern):
    m = len(pattern)
    ft = [-1] * m
    k = -1
    for j in range(1, m):
        while k >= 0 and pattern[k+1] != pattern[j]:
            k = ft[k]

        if pattern[k+1] == pattern[j]:
            k += 1

        ft[j] = k

    print('failure table:'.ljust(20), ft)
    return ft


def kmp(pattern, text):
    print('text:'.ljust(20), text)
    print('pattern:'.ljust(20), pattern)

    m = len(pattern)
    n = len(text)
    ft = ff(pattern)
    k = -1
    r = 0
    for i in range(n):
        while k >= 0 and pattern[k + 1] != text[i]:
            k = ft[k]

        if pattern[k + 1] == text[i]:
            k += 1

        if k+1 == m:
            r += 1
            print(f'match {r} at i={i}:'.ljust(20), f'{text[:i-m + 1]}[[{pattern}]]{text[i+1:]}')
            k = ft[k]
    return r


kmp('aabaabaab', 'aabaabaabaabaabaab')


def compute_prefix_table(p):
    m = len(p)
    a = [None] * m
    a[0] = -1
    k = -1
    for i in range(1, m):
        while k >= 0 and not p[i] == p[k+1]:
            k = a[k]
        if p[i] == p[k+1]:
            k += 1
        a[i] = k
    return a


def kmp_string_search(p, t):
    m = len(p)
    n = len(t)
    a = compute_prefix_table(p)
    k = -1
    for i in range(n):
        while k >= 0 and not t[i] == t[k+1]:
            k = a[k]
        if t[i] == t[k+1]:
            k += 1
        if k+1 == m:
            print(f'result found at index {i}')
            k = a[k]


kmp_string_search('aabaabaab', 'aabaabaabaabaabaab')




























