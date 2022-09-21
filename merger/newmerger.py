import ezdxf
from ezdxf.addons import Importer
from ezdxf import colors, bbox
from ezdxf.math import Matrix44

import json
from os import listdir
from os.path import isfile, join
import sys
import random

# colorlist for randomly color into dxf layers
colorlist = [
    ("LAYER_RED", colors.RED),
    ("LAYER_YELLOW", colors.YELLOW),
    ("LAYER_GREEN", colors.GREEN),
    ("LAYER_CYAN", colors.CYAN),
    ("LAYER_BLUE", colors.BLUE),
    ("LAYER_MAGENTA", colors.MAGENTA),
]


def merge(source, target):
    """
    Use importer to add source dxf into target dxf
    """
    importer = Importer(source, target)
    # import all entities from source modelspace into target modelspace
    importer.import_modelspace()
    # import all required resources and dependencies
    importer.finalize()


def assign_layer(doc, layer_props):
    """
    Assign layer inside dxf target based on new layer (layername)
    Set active entity for dxf layer with equivalent layername
    """
    layer_name, layer_color = layer_props
    try:
        new_layer = doc.layers.new(layer_name)
    except ezdxf.DXFTableEntryError:
        print(f"layer '{layer_name}' already exist")
        return
    new_layer.dxf.color = layer_color
    for entity in doc.modelspace():
        entity.dxf.layer = layer_name


# opening JSON file
jsondata = json.load(open("data.json"))

if jsondata["use_filelist"]:
    # it use the hardcode file list from data.json
    files = jsondata["filelist"]
else:
    # alternative way of get filelist only using pathin (no filename hardcoding), only dxf files
    files = [
        f
        for f in listdir(jsondata["pathin"])
        if isfile(join(jsondata["pathin"], f))
        if f.lower().endswith(".dxf")
    ]

# empty target dxf
target = ezdxf.new()
target_dxf = target
cache = bbox.Cache()

# merger with filelist
for filename in files:
    # path prepare
    print("input  ->", filename)
    filename = jsondata["pathin"] + filename

    layer_props = random.choice(colorlist)
    append_dxf = ezdxf.readfile(filename)

    # assign layer
    assign_layer(append_dxf, layer_props)

    # merge
    merge(append_dxf, target_dxf)

# save merged dfx target
try:
    print("target ->", jsondata["targetfile"])
    target.saveas(jsondata["pathout"] + jsondata["targetfile"])
except Exception as e:
    print("Error -> ", e.__class__)
