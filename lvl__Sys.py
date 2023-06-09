from simulador_rpg import enemy, player_class

expPool = 0

def expWon():
    
    enemyExp = enemy.exp * (enemy.level * 0.5 + 1)

    player_class.exp = player_class.exp + enemyExp

    if player_class.exp > expPool:

        player_class.level += 1
        
        player_class.exp = player_class.exp - expPool

        expPool = expPool * 1.1

    return 1

# def playerLevel (playerExp, enemyExp):