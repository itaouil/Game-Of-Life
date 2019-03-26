# Game-Of-Life
GSoC Game Of Life

## Getting started

The code implementation is based on **robertmartin8** implementation of the game.

### Install stuff

Install numpy and matplotlib
```bash
pip install numpy matplotlib
```

Clone the repo

```bash
git clone https://github.com/itaouil/Game-Of-Life.git
```

Move into the directory that was just created (either through your filesystem or with `cd GameOfLife`), and you are ready to go!

That's all. You can interface with GameOfLife via the command line. As an example, try running the following:

```bash
python3 main.py
```

## User guide

If at any time you need a quick reference, just run the `help` command:

```bash
python main.py --help
```

Which will give you the following

```bash
usage: main.py [-h] [--grid-size GRID_SIZE] [-seed SEED] [-n N]
               [-quality QUALITY] [-cmap CMAP] [-interval INTERVAL]
               [--seed-position SEED_POSITION]

optional arguments:
  -h, --help            show this help message and exit
  --grid-size GRID_SIZE
                        comma-separated dimensions of grid (x by y)
  -seed SEED            seed config
  -n N                  number of grid iterations
  -quality QUALITY      image quality in DPI
  -cmap CMAP            colour scheme
  -interval INTERVAL    interval (in milliseconds) between iterations
  --seed-position SEED_POSITION
                        comma-separated coordinates of seed
```
