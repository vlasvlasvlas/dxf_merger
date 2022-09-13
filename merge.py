import sys
import ezdxf
from ezdxf.addons import Importer
import json

def merge(source, target):
    """
    input: source file (with dxf data), target data (empty shell where you add dxf data from source)
    output: accumulative dxf data on target file
    """
    try:
        source = ezdxf.readfile(source)
        importer = Importer(source, target)
        # import all entities from source modelspace into target modelspace
        importer.import_modelspace()
        # import all required resources and dependencies
        importer.finalize()
    except Exception as e:
        print("Error -> ",e.__class__)

# opening JSON file
jsondata = json.load(open('data.json'))
files = jsondata['filelist']

# empty target dxf
target = ezdxf.new()

# merger with dict
for file in files:
    print(file)
    merge(jsondata['pathin']+file,target)

# save merge
try:
    target.saveas(jsondata['pathout']+jsondata['targetfile'])
except Exception as e:
    print("Error -> ",e.__class__)