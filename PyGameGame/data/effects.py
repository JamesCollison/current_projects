import pygame
import os


class Effect(pygame.sprite.Sprite):
    def __init__(self, _screen, *groups):
        self.screen = _screen
        pygame.sprite.Sprite.__init__(self, *groups)


class Fade(Effect):
    def __init__(self, color, fill_rate, screen, *groups):
        super(Fade, self).__init__(screen, *groups)
        self.color = color
        self.fill_rate = fill_rate
        self.alive = True
        self.image = pygame.Surface(screen.get_size())
        self.rect = self.image.get_rect()
        self.image.fill(color, self.rect)
        self.next = None


class FadeOut(Fade):
    def __init__(self, *args):
        super().__init__(*args)
        self.transparency = 0
        self.max_transparency = 255

    def update(self):
        self.transparency += self.fill_rate
        self.image.set_alpha(self.transparency)
        if self.transparency >= self.max_transparency:
            self.kill()
            self.screen.fill(pygame.Color(self.color))
            # this stops screen from not being faded in on last frame occasionally


class FadeIn(Fade):
    def __init__(self, *args):
        super().__init__(*args)
        self.transparency = 255
        self.min_transparency = 0

    def update(self):
        self.transparency -= self.fill_rate
        self.image.set_alpha(self.transparency)
        if self.transparency <= self.min_transparency:
            self.kill()


class CursorEffect(Effect):
    def __init__(self, pos, _screen, img):
        super(CursorEffect, self).__init__(_screen)
        self.index = 0
        self.img = img
        self.pos = pos
        self.alive = True

    def draw(self):
        print(self.index)
        self.screen.blit(self.img[self.index], (self.pos[0] - 16, self.pos[1] - 16))

    def update(self):
        self.index += 1
        if self.index == 3:
            self.kill()

    def kill(self):
        self.alive = False
        del self


class CursorClickEffect(CursorEffect):
    def __init__(self, pos, _screen):
        path = os.path.join("..", "..", "resources", "images", "system", "t_click_1.png")
        img1 = pygame.image.load(path)
        img2 = pygame.image.load("../../resources/images/system/t_click_2.png")
        img3 = pygame.image.load("../../resources/images/system/t_click_3.png")
        img1.set_colorkey(pygame.Color(255, 0, 255))
        img2.set_colorkey(pygame.Color(255, 0, 255))
        img3.set_colorkey(pygame.Color(255, 0, 255))
        img = [img1, img2, img3]
        super().__init__(pos, _screen, img)


# if __name__ == "__main__":
#     screen = pygame.display.set_mode((500, 500))
#     clock = pygame.time.Clock()
#
#
#
#     f = FadeOut(pygame.Color("white"), 25, screen)
#     y = FadeIn(pygame.Color("white"), 25, screen)
#
#     f.next = y
#     y.next = f
#
#     active = f
#     c = None
#     while True:
#
#
#         active.draw()
#         active.update()
#         if c:
#             if c.alive:
#                 c.draw()
#                 c.update()
#         if active.alive is False:
#             active = active.next
#             active.alive = True
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 c = CursorClickEffect(event.pos, screen)
#
#
#
#
#         pygame.display.update()
#         clock.tick(10)

