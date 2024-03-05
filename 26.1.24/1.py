n = int(input().strip())

def digits(n):
    return sum(int(digit) for digit in str(n))

def best_divisors(n):
    best_divisor = 1
    sum = 1


    for i in range(2, n + 1):
        if n % i == 0:
            current_sum = digits(i)
            if current_sum > sum or (current_sum == sum and i < best_divisor):
                sum = current_sum
                best_divisor = i       
    return best_divisor

print(best_divisors(n))
