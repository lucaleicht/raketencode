import pygame
import time
import sys

# Display-Manager für statische Nachrichten und einfache Launch-Animation
# Assumes a 480x320 display (rotate if needed)

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialisierung
pygame.init()
# Fullscreen oder feste Größe
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 320
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Raketenmission")

# Schriftart laden (Systemfont oder eigene ttf-Datei)
FONT_SIZE = 32
try:
    font = pygame.font.SysFont('Courier', FONT_SIZE)
except:
    font = pygame.font.Font(None, FONT_SIZE)

# Rocket shape for animation (triangle)
ROCKET_WIDTH = 40
ROCKET_HEIGHT = 60


def show_message(text, duration=2):
    """
    Zeigt einen zentrierten Text für eine bestimmte Dauer an.
    :param text: Textinhalt
    :param duration: Anzeigedauer in Sekunden
    """
    screen.fill(BLACK)
    # Render Zeilenumbruch, falls zu lang
    lines = text.split('\n')
    total_height = len(lines) * FONT_SIZE
    y_offset = (SCREEN_HEIGHT - total_height) // 2
    for line in lines:
        surface = font.render(line, True, WHITE)
        rect = surface.get_rect(center=(SCREEN_WIDTH // 2, y_offset + FONT_SIZE // 2))
        screen.blit(surface, rect)
        y_offset += FONT_SIZE
    pygame.display.update()
    # Handle events to keep OS happy
    start = time.time()
    while time.time() - start < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        time.sleep(0.1)


def show_launch_animation(frames=20, speed=0.05):
    """
    Einfache Raketen-Start-Animation:
    Die Rakete (Dreieck) bewegt sich von unten nach oben.
    :param frames: Anzahl der Frames
    :param speed: Pause zwischen Frames in Sekunden
    """
    for i in range(frames):
        screen.fill(BLACK)
        # Raketen-Position berechnen
        x = SCREEN_WIDTH // 2
        # Y-Achse: von unten (SCREEN_HEIGHT) nach oben (0)
        y = SCREEN_HEIGHT - (i / frames) * (SCREEN_HEIGHT + ROCKET_HEIGHT)
        # Zeichne Rakete als gefülltes Dreieck
        point1 = (x, max(0, y))
        point2 = (x - ROCKET_WIDTH // 2, min(SCREEN_HEIGHT, y + ROCKET_HEIGHT))
        point3 = (x + ROCKET_WIDTH // 2, min(SCREEN_HEIGHT, y + ROCKET_HEIGHT))
        pygame.draw.polygon(screen, WHITE, [point1, point2, point3])
        pygame.display.update()
        # Events verarbeiten
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        time.sleep(speed)
    # Nach Ende Animation kurz stehen bleiben
    time.sleep(1)


if __name__ == '__main__':
    # Einfacher Test
    show_message("Test: Willkommen an Bord", duration=2)
    show_launch_animation()
    show_message("Test beendet", duration=2)
    pygame.quit()
