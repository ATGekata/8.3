def min_boats_required(max_weight, fishermen_weights):
    fishermen_weights.sort()
    boats = 0
    left, right = 0, len(fishermen_weights) - 1

    while left <= right:
        if fishermen_weights[left] + fishermen_weights[right] <= max_weight:
            left += 1
        right -= 1
        boats += 1

    return boats

max_weight = int(input("Enter the maximum weight one boat can carry: "))
num_fishermen = int(input("Enter the number of fishermen: "))
fishermen_weights = [int(input()) for _ in range(num_fishermen)]

result = min_boats_required(max_weight, fishermen_weights)
print("Minimum number of boats required:", result)
