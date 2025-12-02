print("Radhe Radhe...\n")
# Py Game....
import pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("X O Game")

white = (255, 255, 255)
black = (0, 0, 0)
size = 200

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

player = "X"  # Use X and O instead of A
font = pygame.font.Font(None, 120)

run = True
while run:
    screen.fill(white)

    # Draw board
    pygame.draw.line(screen, black, (200, 0), (200, 600), 4)
    pygame.draw.line(screen, black, (400, 0), (400, 600), 4)
    pygame.draw.line(screen, black, (0, 200), (600, 200), 4)
    pygame.draw.line(screen, black, (0, 400), (600, 400), 4)

    # Draw X and O
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, black)
                screen.blit(text, (col * size + 60, row * size + 40))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type ==pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // 200
            col = mouse_x // 200

            if row < 3 and col < 3 and board[row][col] == "":
                board[row][col] = player
                player = "O" if player == "X" else "X"

    pygame.display.update()

pygame.quit()