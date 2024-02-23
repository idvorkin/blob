#!python3
# probably skip montage, or recreate it afterwards.

from icecream import ic
import subprocess
import typer
from pathlib import Path
from typing import List, Optional

app = typer.Typer()


def shrink_files(files):
    ic(files)
    new_size = '2048x2040'
    # subprocess
    for f in files:
        if "montage" in f.name:
            continue # skip montage in shrinking.

        info_command = f"identify {f}"
        # Web sucks with HEIC, so convert them.
        f_out = f.name.replace("HEIC","jpg")
        ic(subprocess.run(info_command, shell=True).stdout)
        resize_command = f"""convert {f} -interlace Plane -resize {new_size}\> {f_out}"""
        ic(resize_command)
        o = subprocess.run(resize_command, shell=True)
        print (o.stdout)
        ic(subprocess.run(info_command, shell=True).stdout)


@app.command()
def shrink(user_files:Optional[List[str]]= typer.Argument(None)):
    files = []
    if not user_files:
        user_files = ["*"]

    if len(user_files) == 1:
        files = list(Path(".").glob(user_files[0]))
    else:
        files = [Path(f) for f in user_files]

    shrink_files(files)

if __name__ == "__main__":
    app()
