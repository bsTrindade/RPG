# from simulador_rpg import enemy, player_class

expPool = 0

def expWon(enemyClass, playerClass):
    
    enemyExp = enemyClass.exp * (enemyClass.level * 0.5 + 1)

    playerClass.exp = playerClass.exp + enemyExp

    if playerClass.exp > expPool:

        playerClass.level += 1
        
        playerClass.exp = playerClass.exp - expPool

        expPool = expPool * 1.1


# def playerLevel (playerExp, enemyExp):