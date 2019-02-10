import pygame, sys

class SpriteManager:
    def __init__(self, img_path, img_width, img_height, x_count, y_count):
        """
        img_path: String
            Path of spritesheet image
        img_width: Integer
            Width in pixels of spritesheet
        img_height: Integer
            Height in pixels of spritesheet
        x_count: Integer
            Number of cells in horizontal
        y_count: Integer
            Number of cells in vertical
        """
        # Load information
        self.sheet = pygame.image.load(img_path).convert()
        self.cells = []
        self.img_width = img_width
        self.img_height = img_height
        self.x_count = x_count
        self.y_count = y_count

        # Divide cells
        (w, h) = (self.img_width / x_count, self.img_height / y_count)
        for row in range(y_count):
            for col in range(x_count):
                # Getting rect with starting points and sizes
                cell_rect = pygame.Rect(col * w, row * h, w, h)
                # Getting image from rect
                cell_image = pygame.Surface(cell_rect.size).convert()
                cell_image.blit(self.sheet, (0,0), cell_rect)
                alpha = cell_image.get_at((5,5))
                cell_image.set_colorkey(alpha)
                self.cells.append(cell_image)

class Player:
    def __init__(self):
        self.sheet = {}
        self.current_img = None
        self.current_rect = None

if __name__=='__main__':
    pygame.init()
    size = WIDTH, HEIGHT = (640, 480)
    screen = pygame.display.set_mode(size)
    color = pygame.Color(255, 0, 255, 255)

    FPS = 60
    FPSCLOCK = pygame.time.Clock()

    # Creating a sprite manager and the player sheet
    spriteManager = SpriteManager('sprite_character.png', 576, 385, 12, 8)
    player = Player()
    player.sheet['down'] = spriteManager.cells[0:5]
    player.sheet['left'] = spriteManager.cells[12:17]
    player.sheet['right'] = spriteManager.cells[24:29]
    player.sheet['up'] = spriteManager.cells[36:41]

    player.current_img = player.sheet['down'][-1]
    player.current_rect = player.current_img.get_rect()
    player.current_rect.center = (320, 240)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] != 0:
            player.current_img = player.sheet['up'][-1]
            player.current_rect.y -= 4
        if keys[pygame.K_s] != 0:
            player.current_img = player.sheet['down'][-1]
            player.current_rect.y += 4
        if keys[pygame.K_a] != 0:
            player.current_img = player.sheet['left'][-1]
            player.current_rect.x -= 4
        if keys[pygame.K_d] != 0:
            player.current_img = player.sheet['right'][-1]
            player.current_rect.x += 4

        screen.fill(color)
        screen.blit(player.current_img, player.current_rect)

        pygame.display.flip()
        FPSCLOCK.tick(FPS)
