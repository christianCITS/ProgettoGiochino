import pygame


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
a=60
player_size = (30, 30)  # Dimensioni del rettangolo (larghezza, altezza)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("light blue")
    
    rect=pygame.Rect(player_pos,player_size)
    pygame.draw.rect(screen,"orange",rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 900 * dt
    if keys[pygame.K_s]:
        player_pos.y += 900 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 900 * dt
    if keys[pygame.K_d]:
        player_pos.x += 900 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    if keys[pygame.K_l]:
        if a==60:
            a=120
        elif a==120:
            a=60
            
    dt=clock.tick(a)/1000
    
   


pygame.quit()



    


