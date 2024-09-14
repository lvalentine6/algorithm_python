def solution(numbers, target):
    def dfs(index=0, current_sum=0):
        if index == len(numbers):
            return 1 if current_sum == target else 0

        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])

    return dfs()
