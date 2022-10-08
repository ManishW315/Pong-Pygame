# Imports
import pygame

# Initializing all pygame modules
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Creating Game Window
game_window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Pong Game")
clk = pygame.time.Clock()
font = pygame.font.SysFont("ebrima", 55)
font_1 = pygame.font.SysFont("ariel", 35)

# Text on screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, (x, y))


def text_screen_1(text, color, x, y):
    screen_text = font_1.render(text, True, color)
    game_window.blit(screen_text, (x, y))

# Game main function
def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill((0, 200, 200))
        text_screen("Welcome to Pong", black, 180, 120)
        text_screen("Press SPACE BAR To Play", black, 130, 220)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clk.tick(60)


# Gameloop
def gameloop():
    # Game Specific Variables
    exit_game = False
    winner_1 = False
    winner_2 = False
    player1_x = 30
    player1_y = 170
    player2_x = 750
    player2_y = 170
    player1_x_size = player2_x_size = 20
    player1_y_size = player2_y_size = 140
    ball_x = 400
    ball_y = 230
    ball_size = 15
    fps = 60
    speed = 5
    velocity_ball_x = 0
    velocity_ball_y = 0
    player1_change = 0
    player2_change = 0
    score_1 = 0
    score_2 = 0
    while not exit_game:
        # Player 1 Wins
        if winner_1:
            game_window.fill((255, 215, 0))
            text_screen("Player 1 is the Winner!!!", blue, 115, 150)
            text_screen("Press ENTER", blue, 275, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        # Player 2 wins
        elif winner_2:
            game_window.fill((255, 215, 0))
            text_screen("Player 2 is the Winner!!!", blue, 115, 150)
            text_screen("Press ENTER", blue, 275, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        # Players movement
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        velocity_ball_x = speed
                        velocity_ball_y = speed
                    if event.key == pygame.K_w:
                        player1_change = -10
                    if event.key == pygame.K_s:
                        player1_change = 10
                    if event.key == pygame.K_UP:
                        player2_change = -10
                    if event.key == pygame.K_DOWN:
                        player2_change = 10
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        ball_x -= speed
                        ball_y += speed
                    if event.key == pygame.K_w:
                        player1_change = 0
                    if event.key == pygame.K_s:
                        player1_change = 0
                    if event.key == pygame.K_UP:
                        player2_change = 0
                    if event.key == pygame.K_DOWN:
                        player2_change = 0
            # Ball movement
            if player1_y <= 25:
                player1_y = 25
            if player1_y >= 340:
                player1_y = 340
            if player2_y <= 25:
                player2_y = 25
            if player2_y >= 340:
                player2_y = 340

            if ball_x == player1_x + 30:
                if player1_y + 140 > ball_y > player1_y:
                    velocity_ball_x = -speed

            if ball_x == player2_x - 10:
                if player2_y + 140 > ball_y > player2_y:
                    velocity_ball_x = speed

            if ball_y < 30:
                velocity_ball_y = speed

            if ball_y > 450:
                velocity_ball_y = -speed

            ball_x -= velocity_ball_x
            ball_y += velocity_ball_y
            player1_y += player1_change
            player2_y += player2_change

            if ball_x < player1_x + 30:
                score_2 += 10
                if score_2 > 100:
                    winner_2 = True
                ball_x = 400
                ball_y = 230
                velocity_ball_x = 0
                velocity_ball_y = 0
            if ball_x > player2_x - 10:
                score_1 += 10
                ball_x = 400
                ball_y = 230
                velocity_ball_x = 0
                velocity_ball_y = 0

            # Win condition
            if score_1 > 90:
                winner_1 = True
                print("!!!!!!!!!!!!!!")
            if score_2 > 90:
                winner_2 = True
                print("!!!!!!!!!!!!!!")
            game_window.fill((100, 255, 100))
            text_screen_1("Score: " + str(score_1), blue, 45, 5)
            text_screen_1("Score: " + str(score_2), red, 655, 5)
            pygame.draw.rect(game_window, blue, (player1_x, player1_y, player1_x_size, player1_y_size))
            pygame.draw.rect(game_window, red, (player2_x, player2_y, player2_x_size, player2_y_size))
            pygame.draw.circle(game_window, black, (ball_x, ball_y), ball_size)
        pygame.display.update()
        clk.tick(fps)
    pygame.quit()
    quit()


welcome()
