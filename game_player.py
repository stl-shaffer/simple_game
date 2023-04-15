import pygame

class Player:
    def __init__(self, x, y, width, height, screen_width):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.screen_width = screen_width
        self.is_jumping = False
        self.jump_count = 10
        self.falling = True

    def move_left(self):
        if self.x > 0:
            self.x -= self.velocity

    def move_right(self):
        if self.x < self.screen_width - self.width:
            self.x += self.velocity

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True

    def update(self):
        if self.is_jumping:
            if self.jump_count >= -10:
                neg = 1 if self.jump_count > 0 else -1
                self.falling = neg == -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10
                self.falling = True

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))

    def on_platform_collision(self, platform):
        if self.falling and platform.x <= self.x <= platform.x + platform.width:
            self.y = platform.y - self.height
            self.is_jumping = False
            self.jump_count = 10
            self.falling = False
