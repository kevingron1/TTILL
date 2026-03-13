import os
import random
import pygame

pygame.init()

# Skärm
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird Game")

clock = pygame.time.Clock()
FPS = 60

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_PATH = os.path.join(BASE_DIR, "assets")
HIGHSCORE_FILE = os.path.join(BASE_DIR, "highscore.txt")

def load_image(name):
    return pygame.image.load(os.path.join(ASSET_PATH, name)).convert_alpha()

# Highscore
def load_highscore():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as file:
            return int(file.read())
    return 0

def save_highscore(value):
    with open(HIGHSCORE_FILE, "w") as file:
        file.write(str(value))

# Assets
bird_img = load_image("bird.png")
pipe_img = load_image("pipe.png")
bg_img = load_image("background.png")
ground_img = load_image("ground.png")

ground_y = SCREEN_HEIGHT - ground_img.get_height()
GROUND_SPEED = 3
ground_x = 0

# Fågel
bird_x = 80
bird_y = SCREEN_HEIGHT // 2 - 100
bird_velocity = 0
GRAVITY = 0.5
JUMP_STRENGTH = -8

# Rör
PIPE_GAP = 150
PIPE_SPEED = 3
pipes = []

def spawn_pipe():
    gap_y = random.randint(100, SCREEN_HEIGHT - 100 - PIPE_GAP)

    top_pipe_rect = pipe_img.get_rect(midbottom=(SCREEN_WIDTH + 50, gap_y))
    bottom_pipe_rect = pipe_img.get_rect(midtop=(SCREEN_WIDTH + 50, gap_y + PIPE_GAP))

    return {"top": top_pipe_rect, "bottom": bottom_pipe_rect, "passed": False}

PIPE_EVENT = pygame.USEREVENT
pygame.time.set_timer(PIPE_EVENT, 1500)

# Score
score = 0
highscore = load_highscore()

font = pygame.font.SysFont(None, 40)

# Knappar
start_button = pygame.Rect(SCREEN_WIDTH//2 - 80, SCREEN_HEIGHT//2 - 40, 160, 60)
restart_button = pygame.Rect(SCREEN_WIDTH//2 - 90, SCREEN_HEIGHT//2 + 20, 180, 60)
quit_button = pygame.Rect(SCREEN_WIDTH//2 - 90, SCREEN_HEIGHT//2 + 100, 180, 60)

# Game State
game_state = "START"
running = True

# Reset
def reset_game():
    global bird_y, bird_velocity, pipes, score
    pipes.clear()
    bird_y = SCREEN_HEIGHT // 2 - 100
    bird_velocity = 0
    score = 0

# Loop
while running:
    clock.tick(FPS)

    bird_rect = bird_img.get_rect(center=(bird_x, bird_y))
    mouse_pos = pygame.mouse.get_pos()

    # Input
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_state == "PLAYING":
                bird_velocity = JUMP_STRENGTH

        if event.type == pygame.MOUSEBUTTONDOWN:

            if game_state == "START":
                if start_button.collidepoint(mouse_pos):
                    reset_game()
                    game_state = "PLAYING"
                    bird_velocity = JUMP_STRENGTH

            elif game_state == "GAME_OVER":

                if restart_button.collidepoint(mouse_pos):
                    reset_game()
                    game_state = "PLAYING"

                if quit_button.collidepoint(mouse_pos):
                    running = False

        if event.type == PIPE_EVENT and game_state == "PLAYING":
            pipes.append(spawn_pipe())

    # Uppdatera
    if game_state == "PLAYING":

        bird_velocity += GRAVITY
        bird_y += bird_velocity

        rotated_bird = pygame.transform.rotate(bird_img, -bird_velocity * 3)
        bird_rect = rotated_bird.get_rect(center=(bird_x, bird_y)).inflate(-4, -4)

        for pipe in pipes:

            pipe["top"].x -= PIPE_SPEED
            pipe["bottom"].x -= PIPE_SPEED

            top_hitbox = pipe["top"].inflate(-6, -10)
            bottom_hitbox = pipe["bottom"].inflate(-6, -10)

            if bird_rect.colliderect(top_hitbox) or bird_rect.colliderect(bottom_hitbox):

                if score > highscore:
                    highscore = score
                    save_highscore(highscore)

                game_state = "GAME_OVER"

            if pipe["top"].right < bird_x and not pipe["passed"]:
                pipe["passed"] = True
                score += 1

        pipes = [p for p in pipes if p["top"].right > 0]

        ground_x -= GROUND_SPEED
        if ground_x <= -SCREEN_WIDTH:
            ground_x = 0

        if bird_rect.top <= 0 or bird_rect.bottom >= ground_y:

            if score > highscore:
                highscore = score
                save_highscore(highscore)

            game_state = "GAME_OVER"

    else:
        rotated_bird = bird_img

    # Rita
    screen.blit(bg_img, (0, 0))

    for pipe in pipes:
        screen.blit(pygame.transform.flip(pipe_img, False, True), pipe["top"])
        screen.blit(pipe_img, pipe["bottom"])

    screen.blit(rotated_bird, bird_rect)

    screen.blit(ground_img, (ground_x, ground_y))
    screen.blit(ground_img, (ground_x + SCREEN_WIDTH, ground_y))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - 60, 45))

    # Start Meny
    if game_state == "START":

        color = (200,200,200) if start_button.collidepoint(mouse_pos) else (255,255,255)
        pygame.draw.rect(screen, color, start_button, border_radius=10)

        text = font.render("START", True, (0,0,0))
        screen.blit(text, (start_button.x + 35, start_button.y + 15))

        highscore_text = font.render(f"Highscore: {highscore}", True, (255,255,255))
        screen.blit(highscore_text, (SCREEN_WIDTH//2 - 90, start_button.y + 80))

    # Game Over Meny
    if game_state == "GAME_OVER":

        over_text = font.render("GAME OVER", True, (255,255,255))
        screen.blit(over_text, (SCREEN_WIDTH//2 - 90, SCREEN_HEIGHT//2 - 60))

        # Restart knapp
        color = (200,200,200) if restart_button.collidepoint(mouse_pos) else (255,255,255)
        pygame.draw.rect(screen, color, restart_button, border_radius=10)

        restart_text = font.render("RESTART", True, (0,0,0))
        screen.blit(restart_text, (restart_button.x + 30, restart_button.y + 15))

        # Quit knapp
        color = (200,200,200) if quit_button.collidepoint(mouse_pos) else (255,255,255)
        pygame.draw.rect(screen, color, quit_button, border_radius=10)

        quit_text = font.render("QUIT", True, (0,0,0))
        screen.blit(quit_text, (quit_button.x + 50, quit_button.y + 15))

        highscore_text = font.render(f"Highscore: {highscore}", True, (255,255,255))
        screen.blit(highscore_text, (SCREEN_WIDTH//2 - 90, quit_button.y + 80))

    pygame.display.update()

pygame.quit()