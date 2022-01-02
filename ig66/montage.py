#!python3
# probably skip montage, or recreate it afterwards.

from os import listdir
from os.path import isfile, join
from icecream import ic
import subprocess
import typer
from loguru import logger

app = typer.Typer()

path = './'

# When tiling we want a maximum of 5 on a row,
# But we want to have our rows be as full as possible.
# So if you have 5 elements, you are len 5

@app.command()
def test():
    for i in range(1,20):

        horizontal_tiles =    compute_length(i)
        rows = i/horizontal_tiles
        ic (i,horizontal_tiles , rows)


MAX_TILE = 4
# Not sure why algo isn't working, do it manually
def compute_length(count):
    if count <= MAX_TILE:
        return count
    if count  == 5:
        return  3
    if count  == 6:
        return  3
    if count  == 7:
        return  4
    if count  == 8:
        return  3
    if count  == 9:
        return  3

    return MAX_TILE

def compute_length_tobuild(count):

    # count is now greator
    # subtract a tile, if divisor hasn't changed, keep going till it does
    if count <= MAX_TILE:
        return count

    best_tile = MAX_TILE
    best_divisor = count//best_tile
    current_divisor = best_divisor
    ic (" I ", best_divisor, current_divisor, best_tile)
    while best_divisor == current_divisor and best_tile > 0:
        best_tile -=1
        current_divisor = count // best_tile
        ic ("  L", best_divisor, current_divisor, best_tile)

    return best_tile + 1


@app.command()
def make():
    ic(subprocess.run("rm montage.jpg", shell=True).stdout)
    files = [f for f in listdir(path) if isfile(join(path, f))]

    count_files = len(files)
    ic(subprocess.run("rm montage.jpg", shell=True).stdout)
    horizontal_tiles = compute_length(len(files))
    rows = len(files) // horizontal_tiles
    ic (len(files), horizontal_tiles, rows)
    montage_cmd = f"montage -auto-orient -limit memory 999MB -geometry 512x512 -tile {horizontal_tiles}x * montage.jpg"
    ic(subprocess.run(montage_cmd, shell=True).stdout)

@logger.catch
def wrap_main():
    app()

if __name__ == "__main__":
    wrap_main()

