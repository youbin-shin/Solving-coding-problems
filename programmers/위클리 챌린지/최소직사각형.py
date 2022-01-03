def solution(sizes):
    max_row = 0
    max_col = 0
    for r, c in sizes:
        if r < c: r, c = c, r
        if max_row < r: max_row = r
        if max_col < c: max_col = c
    return max_row * max_col