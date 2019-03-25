"""
    Game Of Life class implementation

    Python implementation using standard
    Python3 and numpy for the algorithm
    implementation and matplotlib for the
    animations (withing the grid).

    GSoC 2019 code challenge.
"""

# Import modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Import seed configurations
from config import seeds

class GameOfLife:

    def __init__(self, grid_size):
        """
            Class constructor
        """
        # Initialise world (grid)
        self.grid = np.zeros(grid_size)

    def cell_survival(x, y):
        """
            Checks if the cell at position
            (x,y) survives or not based on
            the game's rules.

            Arguments:
                :param x: x coordinate in the grid
                :type x: int

                :param y: y coordinate in the grid
                :type y: int
        """
        # Compute number of living cells around (x,y)
        neighbours = np.sum(self.grid[x-1:x+2, y-1:y+2] - self.grid[x, y])

        # Apply rules of the game
        if self.grid[x, y] and not (2 <= neighbours <= 3):
            return 0
        elif neighbours == 3:
            return 1
        return self.grid[x, y]

    def grid_check():
        """
            Cell checking for all the grid

            Returns:
                :return: updated universe of cells
                :rtype: np.ndarray
        """
        # Deep copy of the self grid for new computation
        new_grid = np.copy(self.grid)

        # Apply game's rule over the whole grid
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                new_grid[i, j] = self.cell_survival(i, j, self.grid)

        # Return new grid
        return new_grid

    def animate(seed, seed_position, quality=200, cmap="Purples", n_generations=50, interval=300):
        """
            Animation (but quite like Disney, sorry)

            Arguments:
                :type universe_size: tuple (int, int)
                :param seed: initial starting array
                :type seed: list of lists, np.ndarray
                :param seed_position: coordinates where the top-left corner of the seed array should
                                      be pinned
                :type seed_position: tuple (int, int)
                :param cmap: the matplotlib cmap that should be used
                :type cmap: str
                :param n_generations: number of universe iterations, defaults to 30
                :param n_generations: int, optional
                :param interval: time interval between updates (milliseconds), defaults to 300ms
                :param interval: int, optional
                :param save: whether the animation should be saved, defaults to False
                :param save: bool, optional
        """
        # Starting seed point
        x_start, y_start = seed_position[0], seed_position[1]

        # Initial config (seed)
        seed_array = np.array(seeds[seed])

        # Determine endpoints of the seed
        x_end, y_end = x_start + seed_array.shape[0], y_start + seed_array.shape[1]

        # Inject seed in the grid
        self.grid[x_start:x_end, y_start:y_end] = seed_array

        # Animation baby
        fig = plt.figure(dpi=quality)
        plt.axis("off")
        ims = []

        # Iterate over grid
        for i in range(n_generations):
            ims.append((plt.imshow(universe, cmap=cmap),))
            universe = generation(universe)

        im_ani = animation.ArtistAnimation(fig,
                                           ims,
                                           interval=interval,
                                           repeat_delay=3000,
                                           blit=True)
