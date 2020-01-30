
def find_long_over_lap(string):  # "abbc" -> 2, "adddaabaa" -> 3

    a, long_count = 0, 0

    for x in string:

        if x == a:
            count += 1
            if long_count < count:
                long_count = count
        if x != a:
            count = 1
        a = x

    return long_count

