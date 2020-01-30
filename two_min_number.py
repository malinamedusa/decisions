def two_min_number(array) -> int:  # Returns the smallest product of two numbers in an array

    min1, min2, two_max, current_key = 0, 0, 0, 0

    for key, value in enumerate(array):
        if value < min1 or min1 == 0:
            min1 = value
            current_key = key

        if (min2 >= value >= min1 or min2 == 0) and current_key != key:
            min2 = value

        if value > two_max or max == 0:
            two_max = value

    return min(min1 * min2, min1 * two_max, min1 * two_max, min1 * min2)

