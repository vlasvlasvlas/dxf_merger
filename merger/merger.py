import sys
import ezdxf
from ezdxf.addons import Importer
import json
from os import listdir
from os.path import isfile, join

"""
The idea of this script is to merge n dxf files (from pathin) into a target dxf file (into pathout)
"""


def merge(source, target):
    """
    input: source file (with dxf data), target data (empty shell where you add dxf data from source)
    output: accumulative dxf data on target file
    """
    try:
        source = ezdxf.readfile(source)

    except ezdxf.DXFError as e:
        print("\n" + "*" * 40)
        print("FOUND DXF ERROR: {}".format(str(e)))
        print("*" * 40 + "\n")
        return False

    try:
        importer = Importer(source, target)
        # import all entities from source modelspace into target modelspace
        importer.import_modelspace()
        # import all required resources and dependencies
        importer.finalize()

    except Exception as e:
        print("Error -> ", e.__class__)


# opening JSON file
jsondata = json.load(open("data.json"))

if jsondata["use_filelist"]:
    # it use the hardcode file list from data.json
    files = jsondata["filelist"]
else:
    # alternative way of get filelist only using pathin (no filename hardcoding)
    files = [
        f for f in listdir(jsondata["pathin"]) if isfile(join(jsondata["pathin"], f))
    ]

# empty target dxf
target = ezdxf.new()

# merger with dict
for file in files:
    print("filein ->", file)
    merge(jsondata["pathin"] + file, target)

# save merged dfx target
try:
    print("target ->", jsondata["targetfile"])
    target.saveas(jsondata["pathout"] + jsondata["targetfile"])
except Exception as e:
    print("Error -> ", e.__class__)
