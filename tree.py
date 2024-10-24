import pygame


class Tree:

    def __init__(self):

        super().__init__()
        self.width = 500
        self.height = 500
        self.x_p = 700
        self.y_p = 600
        self.tree_a = pygame.transform.scale(
            pygame.image.load(f"./assets/tree/Tree_1_128b.png"),
            (self.width, self.height),
        )

    def tree_1(self):
        return self.tree_a
