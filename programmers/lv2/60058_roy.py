def solution(p):
    answer = ''

    def is_complite(p):
        st = []
        for i in p:
            if i == '(':
                st.append('(')
            elif st:
                st.pop()
        return True if not st else False

    def separate_str(ss):
        nonlocal answer
        if ss == '':
            return ''

        result_str = ''
        stack = []
        cnt = 0
        u = ''
        v = ''
        for idx, i in enumerate(ss):
            stack.append(i)

            if i == '(':
                cnt += 1
            else:
                cnt -= 1

            if idx > 0 and cnt == 0:
                u = ss[:idx + 1]
                v = ss[idx + 1:]
                break

        if is_complite(u):
            result_str += u
            result_str += separate_str(v)
        else:
            result_str += remake_str(u, v)

        return result_str

    def remake_str(u, v):
        remake_str = '('
        remake_str += separate_str(v)
        remake_str += ')'

        u = u[1:-1]

        temp = ''
        for i in u:
            if i == '(':
                temp += ')'
            else:
                temp += '('

        remake_str += temp
        return remake_str

    if is_complite(p):
        return p

    answer = separate_str(p)

    return answer
