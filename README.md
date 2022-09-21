


# DXF merger
  <a href="https://github.com/vlasvlasvlas/dxf_merger/actions/workflows/codeql-analysis.yml">
    <img src="https://github.com/vlasvlasvlas/dxf_merger/actions/workflows/codeql-analysis.yml/badge.svg?event=push" alt="CI Badge"/>
  </a>
<img width="400" alt="DXF Merger" src="https://user-images.githubusercontent.com/4071796/190007423-9e796567-4bf9-4c56-8d1c-388fd69a0f4c.png">
<img width="400" alt="DXF Merger" src="https://user-images.githubusercontent.com/4071796/191415102-54fb53ad-273d-4046-b308-453f021c4de8.png">

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

## TO-DO & Notes

- unit test transformation.
- maybe transform script into Class so i think ll be easier to reuse / include into a data pipeline.

- Added layers, each new dxf data is imported into a new independent layer.
