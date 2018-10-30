def row_sum_odd_numbers(n):
    start = n ** 2 + (n - 1)
    x = start
    y = 0
    for num in range(1, n):
        x = x - 2
    i = sum(range(x,start+1,2))
    return(i)