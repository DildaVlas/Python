def max_evaluation(heights, K):
    max_sum = current_sum = sum(heights[:K])
    for i in range(K, len(heights)):
        current_sum += heights[i] - heights[i - K]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


def read_input(filename):
    with open(filename, 'r') as file:
        N, K = map(int, file.readline().split())
        heights = [int(file.readline()) for _ in range(N)]
    return heights, K


# Пример использования
heights_A, K_A = read_input('data/27-170a.txt')
heights_B, K_B = read_input('data/27-170.txt')

max_eval_A = max_evaluation(heights_A, K_A)
max_eval_B = max_evaluation(heights_B, K_B)

print(f"{max_eval_A} {max_eval_B}")
