"""
    Keep calm, it is just a main.

    By the way, I usually comment properly
    the code so dont worry about that :).
"""

# Import modules
import argparse
from game_of_life import GameOfLife

if __name__ == "__main__":
    # Create command line parser
    parser = argparse.ArgumentParser()

    # Grid size
    parser.add_argument(
        "--grid-size", type=str, default="100, 100", help="comma-separated dimensions of grid (x by y)"
    )

    # Seed configurations
    parser.add_argument(
        "-seed", type=str, default="infinite", help="seed config"
    )

    # Grid iterations
    parser.add_argument(
        "-n", type=int, default=50, help="number of grid iterations"
    )

    # Image quality
    parser.add_argument(
        "-quality", type=int, default=100, help="image quality in DPI"
    )

    # CMAP type
    parser.add_argument(
        "-cmap", type=str, default="Purples", help="colour scheme"
    )

    # Interval (animation)
    parser.add_argument(
        "-interval",
        type=int,
        default=300,
        help="interval (in milliseconds) between iterations",
    )

    # Seed position
    parser.add_argument(
        "--seed-position",
        type=str,
        default="40,40",
        help="comma-separated coordinates of seed",
    )

    # Parse from command line
    args = parser.parse_args()

    # Create game instance
    tuple_size = (int(args.grid_size.split(",")[0]), int(args.grid_size.split(",")[1]))
    print("Grid size: ", tuple_size)
    gol = GameOfLife(tuple_size)

    # Run animation
    seed_pos = (int(args.seed_position.split(",")[0]), int(args.seed_position.split(",")[1]))
    print("Seed pos: ", seed_pos)
    print(args.seed)
    gol.animate(seed=args.seed,
                quality=args.quality,
                cmap=args.cmap,
                seed_position=seed_pos,
                n_generations=args.n,
                interval=args.interval)
