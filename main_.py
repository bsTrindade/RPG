import pygame, sys, narrator
import game as gm
from time import sleep


pygame.init()
pygame.display.set_caption("Trindade's Quest")
pygame.display.set_icon(pygame.image.load('images/icon.png'))

screen_X = 1280
screen_Y = 720
screen = pygame.display.set_mode((screen_X, screen_Y))
clock = pygame.time.Clock()
running = True

#COLOR PALLET
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (244, 195, 80)

#FILES
MENU_IMAGE = 'images/main_menu.png'

GROUND_IMAGE = 'images/main_menu.png'

MAIN_MENU_THEME_SONG = 'sounds/main_menu.mp3'

MAIN_MENU_ACCEPT = 'sounds/menu_accept.wav'

MAIN_MENU_RETURN = 'sounds/menu_return.mp3'

TITLE_FONT = pygame.font.SysFont(None, 100, True, True)

MENU_FONT = pygame.font.SysFont(None, 30)

MENU_BACKGROUND = pygame.transform.scale_by(pygame.Surface.convert(pygame.image.load(MENU_IMAGE)), 0.42)

GROUND = pygame.image.load(GROUND_IMAGE)

FPS = pygame.time.Clock()

click = False

class Background(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.background_image = MENU_BACKGROUND
        self.background_Y = 0
        self.background_X = 0

    def render(self):
        screen.blit(self.background_image,(self.background_X, self.background_Y))

class Ground(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = GROUND
        self.rect = self.image.get_rect(center = ((screen_X / 2), (screen_Y / 2)))

    def render(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

def draw_text(text, font, color, surface, x, y):
    text_object = font.render(text, 1, color)
    text_rect = text_object.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_object, text_rect)
    return text_rect

def main_menu():

    pygame.mixer.set_num_channels(3)

    pygame.mixer.music.load(MAIN_MENU_THEME_SONG)

    pygame.mixer.music.play()

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                        
                        click = True
    

        screen.fill(color='#000000')

        pygame.Surface.blit(screen, MENU_BACKGROUND, [0, 0])

        draw_text("TRINDADE'S QUEST", TITLE_FONT, BLACK, screen, 95, 105)
        draw_text("TRINDADE'S QUEST", TITLE_FONT, YELLOW, screen, 100, 100)
        
        draw_text('NEW GAME', MENU_FONT, BLACK, screen, 110, 260)
        text_new_game = draw_text('NEW GAME', MENU_FONT, WHITE, screen, 115, 255)
        
        draw_text('EXIT', MENU_FONT, BLACK, screen, 110, 300)
        text_exit = draw_text('EXIT', MENU_FONT, WHITE, screen, 115, 295)

        mx, my = pygame.mouse.get_pos()

        if text_new_game.collidepoint((mx, my)):
            draw_text('NEW GAME', MENU_FONT, BLACK, screen, 110, 260)
            draw_text('NEW GAME', MENU_FONT, YELLOW, screen, 115, 255)
            if click:

                sound = pygame.mixer.Sound(MAIN_MENU_ACCEPT)

                pygame.mixer.Sound.play(sound)

                game()

        if text_exit.collidepoint((mx, my)):
            draw_text('EXIT', MENU_FONT, BLACK, screen, 110, 300)
            draw_text('EXIT', MENU_FONT, YELLOW, screen, 115, 295)

            if click:

                sound = pygame.mixer.Sound(MAIN_MENU_ACCEPT)

                pygame.mixer.Sound.play(sound)

                sleep(.17)

                pygame.quit()

                sys.exit()

        click = False

        FPS.tick(60)

        pygame.display.flip()

def screen_nattarion(text):

    narrating = True

    text_to_draw = ''

    while narrating:

        for l in range(len(text)):

                text_to_draw = text_to_draw + text[l]

                draw_text(text_to_draw, MENU_FONT, WHITE, screen, 60, 60)

                pygame.display.update()

                sleep(.1)

        narrating = False

def skip_text():

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                narrating_text = False
                return narrating_text
            
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                narrating_text = False
                return narrating_text

def game():

    while True:
        
        screen.fill(color=BLACK)

        text_rectantangle = pygame.draw.rect(screen, WHITE, (50, 50, 500, 100), 2, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen_nattarion('TESTANDO COM UM TEXTO BEM GRANDÃO PARA VER SE O PROMPT ESTÁ ESCREVENDO')

        pygame.display.flip()

        FPS.tick(60)
        
def game_teste():

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()
        # fill the screen with a color to wipe away anything from last frame
        screen.fill(color='#000000')

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

if __name__ == '__main__':
    main_menu()