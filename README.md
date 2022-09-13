# DXF merger

![imagen](https://user-images.githubusercontent.com/4071796/190007020-ff33033f-e841-4da8-959d-b1773f953d9f.png)

DXF Merger, just a function wrap based on ezdxf to merge n dxf files into a unique new dxf file.

## Requirements

- ezdxf (https://github.com/mozman/ezdxf)
- black code formatter (https://github.com/psf/black)

## How it works

Basically it uses ezdxf's add-on Importer to merge any dxf into an empty shell.

You can edit data.json file to change input folder+files, output folder+file.

## More info

You can get more info at https://ezdxf.readthedocs.io/en/stable/addons/importer.html

## TO-DO

- unit test transformation.
- maybe transform script into Class so i think ll be easier to reuse / include into a data pipeline.
