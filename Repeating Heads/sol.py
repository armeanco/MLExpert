def repeating_heads(n, x):
    coin_toss = 1/2
    chance_of_w = coin_toss**n
    chance_of_l = 1 - chance_of_w
    chance_of_cons_l = chance_of_l**x
    chance_of_cons_w = 1 - chance_of_cons_l
    return [chance_of_cons_w*100, 100/chance_of_cons_w]
