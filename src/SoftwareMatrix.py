import pygame
import numpy as np

class SoftwareMatrix:
    
    def __init__(self, w, h, pix) -> None:
        self.width = w
        self.hight = h
        self.pixelSize = pix
        self.isRunning = True
        self.gap = 1

        pygame.init()
        pygame.display.set_caption("Software LED-Matrix")
        self.screen = pygame.display.set_mode((w*pix + (w+1) * self.gap, h*pix + (h+1) * self.gap))
        self.clock = pygame.time.Clock()

    def Update(self, frame:np.ndarray):
        for y in range(self.hight):
            for x in range(self.width):
                targetX = x * self.pixelSize + (x+1) * self.gap
                targetY = y * self.pixelSize + (y+1) * self.gap
                color = frame[y][x]
                pygame.draw.rect(self.screen, color, pygame.Rect(targetX , targetY, self.pixelSize, self.pixelSize))

        pygame.display.update()
        self.clock.tick(16)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                self.isRunning = False

    