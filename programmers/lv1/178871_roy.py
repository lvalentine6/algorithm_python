def solution(players, callings):
    answer = []

    dic = {player: int(idx) for idx, player in enumerate(players)}

    for calling in callings:
        idx = dic[calling]
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        dic[players[idx]] = idx
        dic[players[idx - 1]] = idx - 1

    answer = players
    return answer
