#!python3
# probably skip montage, or recreate it afterwards.

from os import listdir
from os.path import isfile, join
from icecream import ic
import subprocess

path = './'
files = [f for f in listdir(path) if isfile(join(path, f))]

ic(files)
new_size = '2048x2040'
# subprocess
for f in files:
    if "montage" in f:
        continue # skip montage in shrinking.

    info_command = f"identify {f}"
    # Web sucks with HEIC, so convert them.
    f_out = f.replace("HEIC","jpg")
    ic(subprocess.run(info_command, shell=True).stdout)
    resize_command = f"""convert {f} -interlace Plane -resize {new_size}\> {f_out}"""
    ic(resize_command)
    o = subprocess.run(resize_command, shell=True)
    print (o.stdout)
    ic(subprocess.run(info_command, shell=True).stdout)



