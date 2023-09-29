import pygame


# init
pygame.init()

# variable running game
is_running = True

# membuat display surface object
window_x = 500
window_y = 500
window = pygame.display.set_mode((window_x, window_y))

# object game
# cordinate
x = 250
y = 250

# ukuran
kotak_x = 20
kotak_y = 20

# kecepatan
speed = 10

# game loop
while is_running:
    pygame.time.delay(10)
    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("exiting...")
            is_running = False

    # ambil semua keyboard actio
    keys = pygame.key.get_pressed()

    # ambil kekiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    # ambil kekanan
    if keys[pygame.K_RIGHT] and x < window_x - kotak_x:
        x += speed

    # ambil kebawah
    if keys[pygame.K_UP] and y > 0:
        y -= speed

    # ambil keatas
    if keys[pygame.K_DOWN] and y < window_y - kotak_y:
        y += speed

    # update asset
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 0, 0), (x, y, kotak_x, kotak_y))
    # render ke display
    pygame.display.update()

pygame.quit()
