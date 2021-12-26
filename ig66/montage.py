#!python3
# probably skip montage, or recreate it afterwards.

from os import listdir
from os.path import isfile, join
from icecream import ic
import subprocess

path = './'
ic(subprocess.run("rm montage.jpg", shell=True).stdout)
files = [f for f in listdir(path) if isfile(join(path, f))]

count_files = len(files)
ic(files)
new_size = '2048x2040'
# subprocess

# Tile for number of photos
tile_factor = 5
if len(files) < 5:
    tile_factor = len(files)

# When tiling we want a maximum of 5 on a row,
# But we want to have our rows be as full as possible.
# So if you have 5 elements, you are len 5

# If we have 6 elements, prefer 3 and 3 to 5 and 1.




ic(subprocess.run("rm montage.jpg", shell=True).stdout)
montage_cmd = f"montage -auto-orient -limit memory 999MB -geometry 512x512 -tile {tile_factor}x * montage.jpg"
ic(subprocess.run(montage_cmd, shell=True).stdout)
