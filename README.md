# DXF merger

![imagen](https://user-images.githubusercontent.com/4071796/191414922-a3a52c20-d992-4fc6-9c66-df5720568f23.png)


DXF merger, just a function wrap based on ezdxf to merge n dxf files into a unique new dxf file.

## Requirements

- Python 3.7+

- Virtualenv 

- ezdxf (https://github.com/mozman/ezdxf)

Code formatter used: black (https://github.com/psf/black)

## How it works

Basically it uses ezdxf's add-on Importer to merge any dxf into an empty shell.

You can edit data.json file to change input folder+files, output folder+file:

```
{
    "desc": "files for a demo dxf merger based on ezdxf",
    "pathin": "in/",
    "pathout": "out/",
    "targetfile": "merge.dxf",
    "use_filelist": true,
    "filelist": ["manzana.dxf", "parcela.dxf", "tejido.dxf"],
}
```

## More info

You can get more info at https://ezdxf.readthedocs.io/en/stable/addons/importer.html

## TO-DO

- unit test transformation.
- maybe transform script into Class so i think ll be easier to reuse / include into a data pipeline.
