def test_hard_password(password):  # Testing your password for difficulty

    evaluation = 0  # evaluation min = 4, max = 12
    password = password.replace(' ', '')
    eva_count = 0
    if password.__len__() >= 6:
        print('Lenght OK')
        eva_count += 1
    else:
        print('Lenght Fail')

    if password.__len__() in [6, 7, 8]:
        evaluation += 1
    if password.__len__() in [9, 10]:
        evaluation += 2
    if password.__len__() > 10:
        evaluation += 3

    s_count, n_count, l_count = 0, 0, 0

    for symbol in password:
        if symbol in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_']:
            s_count += 1
        if symbol.isdigit():
            n_count = n_count + 1
        if symbol.isupper():
            l_count = l_count + 1

    if s_count > 0:
        print('Symbol OK')
        eva_count += 1
    else:
        print('Symbol Fail')
    evaluation += min(s_count, 3)
    if n_count > 0:
        print('Number OK')
        eva_count += 1
    else:
        print('Number Fail')
    evaluation += min(n_count, 3)
    if l_count > 0:
        print('Letter OK')
        eva_count += 1
    else:
        print('Letter Fail')
    evaluation += min(l_count, 3)
    percent = '%'
    if eva_count < 4:
        percent_evaluation = (evaluation * 50 / 4)
    else:
        percent_evaluation = ((evaluation - 4) * 50 / 8) + 50
    # 4 = 50%
    # 12 = 100%
    # 8 after 4 = 50%
    print("Your password is complex at %d%s" % (percent_evaluation, percent))
