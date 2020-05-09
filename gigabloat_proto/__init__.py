__version__ = "0.1.0"
from shutil import copy2
import pathlib
import os


def copy_protos(destination):
    if not os.path.isdir(destination):
        os.makedirs(destination)
    this_dir = str(pathlib.Path(__file__).parent.absolute())
    protofile = this_dir + "/gigabloat.proto"
    copy2(protofile, destination)
