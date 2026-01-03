import pygame

# --- Setup ---
pygame.init()
screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Meditation Simulation")
clock  = pygame.time.Clock()

# --- game state ---
hp = 100    # Represents a theoretical hp bar with damage already done
mana = 100  # Represents a theoretical mana bar with mana already used
MAX = 200   # Represents a full bar of hp / mana

is_sitting = False
hp_regen_rate = 10 # per second
mana_regen_rate = 20 # per second

running = True

# --- main loop ---
while running:
    dt = clock.tick(60) / 1000 # seconds since last frame


    # --- input ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                is_sitting = not is_sitting
                state = "Sitting" if is_sitting else "Standing"
                print(f"{state}\n")

            if event.key == pygame.K_q:
                running = False

    # --- regen logic ---
    if is_sitting and (hp < MAX or mana < MAX):
        hp = min(hp + hp_regen_rate * dt, MAX)
        mana = min(mana + mana_regen_rate * dt, MAX)

    # --- render (minimal) ---
    #
    # ORIGINAL
    font = pygame.font.SysFont(None, 26)
    #screen.fill((20, 20, 20))
    #text = font.render(f"HP: {int(hp)}/{MAX} | Mana: {int(mana)}/{MAX}", True, (255, 255, 255))
    #screen.blit(text, (20, 20))
    
    #player_stance = font.render(f"Player: {'Sitting' if is_sitting else 'Standing'}", True, (200, 200, 200))
    #screen.blit(player_stance, (20, 100))
    
    #pygame.display.flip()
    screen.fill((20, 20, 20))  # clear screen

    # HP bar
    pygame.draw.rect(screen, (100,0,0), (20,50,300,25), 2)  # bg
    pygame.draw.rect(screen, (255,0,0), (20,50,(hp/MAX)*300,25))  # fg

    # Mana bar
    pygame.draw.rect(screen, (0,0,100), (20,90,300,25), 2)  # bg
    pygame.draw.rect(screen, (0,0,255), (20,90,(mana/MAX)*300,25))  # fg

    # Sitting/Standing
    state_text = font.render(f"State: {'Sitting' if is_sitting else 'Standing'}", True, (255,255,255))
    screen.blit(state_text, (20, 130))

    pygame.display.flip()




    # --- debug output ---
    print(f"HP: {int(hp)}/{MAX} | Mana: {int(mana)}/{MAX}", end="\r")

pygame.quit()
