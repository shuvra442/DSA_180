# sum of first n natural numbers
def sum_n_numbers (n, sum):
    if n < 1:
        return sum
    
    return sum_n_numbers(n-1, sum + n)

result = sum_n_numbers(5, 0)
print(result)