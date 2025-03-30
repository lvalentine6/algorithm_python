class Node():
    def __init__(self, t, num):
        self.t = t
        self.num = num
        self.child = []


def search(w_cnt, s_cnt, candidates):
    global answer
    if w_cnt >= s_cnt:
        return

    answer = max(answer, s_cnt)

    for i, c in enumerate(candidates):
        nxt_candidates = candidates[:i] + candidates[i + 1:] + c.child
        if c.t == 0:
            search(w_cnt, s_cnt + 1, nxt_candidates)
        else:
            search(w_cnt + 1, s_cnt, nxt_candidates)


def solution(info, edges):
    global answer
    answer = 0

    nodes = [Node(info[i], i) for i in range(len(info))]

    for p, c in edges:
        nodes[p].child.append(nodes[c])

    search(0, 1, nodes[0].child)

    return answer
