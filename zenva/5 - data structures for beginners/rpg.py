import random

player_health = 100
enemy_health = 100

moves = {
    "attack": (0, -10),
    "vampire bite": (5, -5),
    "heal": (15, 0),
    "curse": (-5, -20)
}

def report_status(playerHealth, enemyHealth):
    print(f"""
          Player health: {playerHealth}
          Enemy health: {enemyHealth}
          """)

# Game loop
def Main():
    global player_health, enemy_health
    
    running = True
    current_turn = 1
    while running:

        # Player turn
        if current_turn == 1:
            print("Player's turn")
            valid_input = False
            while not valid_input:
                player_input = input("Choose your move (attack, vampire bite, heal, curse): \n")
                valid_input = player_input.lower() in moves or player_input.lower() == "quit"
                if not valid_input:
                    print("Invalid move. Please try again.")
                
            # Quit the game
            if player_input.lower() == "quit":
                running = False
                print("Thanks for playing!")
                break
            
            Hit(True, player_input.lower())

        elif current_turn == -1:
            print("Enemy's turn")
            # Enemy randomly selects a move
            
            enemy_move = random.choice(list(moves.keys()))
            print(f"Enemy selected move with effects: {enemy_move}")
            Hit(False, enemy_move)
        
        # End of game ?
        game_over, player_won = IsGameOver()
        if game_over:
            running = False    

        # Turn swap
        current_turn *= -1

def Hit(isPlayerAttacking, move):

    global player_health, enemy_health
    attacker_change, target_change = moves[move]

    if (isPlayerAttacking):
        player_health += attacker_change
        enemy_health += target_change
    else:
        enemy_health += attacker_change
        player_health += target_change
        
    report_status(player_health, enemy_health)

def IsGameOver():
    if player_health <= 0:
        print("You have been defeated! Game over.")
        return True, False
    elif enemy_health <= 0:
        print("Congratulations! You have defeated the enemy!")
        return True, True
    return False, False

Main()