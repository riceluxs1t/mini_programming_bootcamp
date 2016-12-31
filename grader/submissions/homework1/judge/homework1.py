def robotopia(l1, a1, l2, a2, lt, at):

    is_done = 0
    ans = None
    for f_num in xrange(1, lt/l1 + 1):

        s_num = (lt - l1*f_num)/l2
        if f_num < 1 or s_num < 1:
            continue
        if (l1 * f_num + l2 * s_num) == lt and (a1 * f_num + a2 * s_num) == at:
            ans = (f_num, s_num)
            is_done += 1
            if is_done > 1:
                break

    if not ans or is_done > 1:
        return '?'
    else:
        return '{0} {1}'.format(ans[0], ans[1])
