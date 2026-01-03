import pygame
import random

# ------- pygame setup -------
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Regenerator")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 22)



# ------ Player Class -------
class Player:
    def __init__(self):
        self.hp = 100
        self.mana = 100
        self.max_hp = 200
        self.max_mana = 200
        self.is_sitting = False
        self.hp_regen_rate = 10
        self.mana_regen_rate = 20

    def toggle_sitting(self):
        self.is_sitting = not self.is_sitting
        
    def update(self, dt):
        if self.is_sitting and (self.hp < self.max_hp or self.mana < self.max_mana):
            self.hp = min(self.hp + self.hp_regen_rate * dt, self.max_hp)
            self.mana = min(self.mana + self.mana_regen_rate * dt, self.max_mana)

    def fish(self):
        has_fish = random.randint(0, 1)

        if has_fish == 0:
            return "Caught a fish!"
        else:
            return "You didn't catch anything!"

    def cheese(self):
        self.hp = 200
        self.mana = 200

# ------ Create Player ------
player = Player()


# ------ UI Constants ------
BAR_WIDTH = 300
BAR_HEIGHT = 20
BAR_X = 20
HP_Y = 50
MANA_Y = 85
FISH_RESULT = "You want to fish?"

# ------ Main Loop ------
running = True

while running:

    dt = clock.tick(60) / 1000

    # ----- Input -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                player.toggle_sitting()

            if event.key == pygame.K_q:
                running = False

            if event.key == pygame.K_f:
                FISH_RESULT = player.fish()

            if event.key == pygame.K_c:
                player.cheese()


    # ----- Update -----
    player.update(dt)

    # Render
    screen.fill("black")
    
    # HP Bar
    hp_fill = (player.hp / player.max_hp) * BAR_WIDTH
    pygame.draw.rect(screen, (80, 0, 0), (BAR_X, HP_Y, BAR_WIDTH, BAR_HEIGHT))
    pygame.draw.rect(screen, (220, 0, 0), (BAR_X, HP_Y, hp_fill, BAR_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (BAR_X, HP_Y, BAR_WIDTH, BAR_HEIGHT), 2)

    # Mana Bar
    mana_fill = (player.mana / player.max_mana) * BAR_WIDTH
    pygame.draw.rect(screen, (0, 0, 80), (BAR_X, MANA_Y, BAR_WIDTH, BAR_HEIGHT))
    pygame.draw.rect(screen, (0, 0, 220), (BAR_X, MANA_Y, mana_fill, BAR_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (BAR_X, MANA_Y, BAR_WIDTH, BAR_HEIGHT), 2)

    # Text
    
    fish_text = font.render(
        f"Fish Bag: {FISH_RESULT}",
        True,
        ("green")
    )

    state_text = font.render(
        f"State: {'Meditating' if player.is_sitting else 'Standing'}",
        True,
        (255, 255, 255)
    )

    instruction_text = font.render(
        """
        1. Press (x) to sit/stand or (q) to quit
        2. Press (f) to fish
        3. Press (c) to eat cheese
        """,
        True,
        (255, 255, 255)
    )

    # Text positions
    screen.blit(fish_text, (BAR_X, 130))
    screen.blit(state_text, (BAR_X, 150))
    screen.blit(instruction_text, (BAR_X, 170))

    # ----- Text test-----
    #header_text = font.render(f"Press (x) to sit/stand or (q) to quit", True, (255, 255, 255))
    #hp_text = font.render(f"HP: {player.hp}", True, (255, 255, 255))
    #mana_text = font.render(f"MANA: {player.mana}", True, (255, 255, 255))
    #screen.blit(header_text, (20, 20))
    #screen.blit(hp_text, (20, 60))
    #screen.blit(mana_text, (20, 80))

    pygame.display.flip()

pygame.quit()    


