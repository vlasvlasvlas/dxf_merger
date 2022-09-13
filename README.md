# DXF merger

<img width="500" alt="DXF Merger" src="https://user-images.githubusercontent.com/4071796/190007423-9e796567-4bf9-4c56-8d1c-388fd69a0f4c.png">


DXF Merger, just a function wrap based on ezdxf to merge n dxf files into a unique new dxf file.

## Requirements

- ezdxf (https://github.com/mozman/ezdxf)

Code formatter used: black (https://github.com/psf/black)

## How it works

Basically it uses ezdxf's add-on Importer to merge any dxf into an empty shell.

You can edit data.json file to change input folder+files, output folder+file.

## More info

You can get more info at https://ezdxf.readthedocs.io/en/stable/addons/importer.html

## TO-DO

- unit test transformation.
- maybe transform script into Class so i think ll be easier to reuse / include into a data pipeline.
