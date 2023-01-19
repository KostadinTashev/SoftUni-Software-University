import math

num_1 = int(input())
num_2 = int(input())
num_1_to = int(input())
num_2_to = int(input())
for n in range(num_1, num_1 + num_1_to + 1):
    for m in range(num_2, num_2 + num_2_to + 1):
        is_n_prime = True
        is_m_prime = True
        sqrt_n = int(math.sqrt(n))
        for i in range(2, sqrt_n + 1):
            if n % i == 0:
                is_n_prime = False
                break
        for j in range(2, int(math.sqrt(m)) + 1):
            if m % j == 0:
                is_m_prime = False
                break
        if is_n_prime and is_m_prime:
            print(f"{n}{m}")
