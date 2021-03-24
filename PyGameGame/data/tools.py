import pygame
import time


def function_timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        execution = func(*args, **kwargs)
        t2 = time.time()
        print(f"{func.__name__} - {(t2-t1)*1000:.5f} ms")
        return execution
    return wrapper


class ImageLoader:
    def __init__(self):
        self.color_key = pygame.Color(255, 0, 255)

    def get_image(self, image, transparent=False):
        try:
            image = pygame.image.load(image)
            image = image.convert()
            if transparent:
                image.set_colorkey(self.color_key)
            return image
        except FileNotFoundError:
            print(f"Failed to load {image}. Directory not found.")


class TextLoader:
    def __init__(self):
        pass

    def get_text(self):
        pass


class SoundLoader:
    def __init__(self):
        pass

    def get_sound(self):
        pass
