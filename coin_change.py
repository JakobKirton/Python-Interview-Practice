n = int(input())
coins = [0.01,0.02,0.10,0.20,0.50,1,2,5,10,20,50]
coins_simple = [1,2,5,10,20,50]

def find_change(n, coins):
    if n < 0:
        return []
    if n == 0:
        return [[]]
    change_combos = []

    for lu_coin in coins:
        combos = find_change(n- lu_coin, coins)
        for combo in combos:
            combo.append(lu_coin)
            change_combos.append(combo)
    return change_combos

print(find_change(n,coins_simple))