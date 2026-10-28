# Learning DVC

A small example of versioning a dataset with DVC and a local remote.

## Why this exists
A first exercise in data version control: tracking changes to a dataset the way Git tracks code.

## What it does
- `mycode.py` writes `data/people_data.csv` and adds rows between runs to create new versions
- DVC tracks the `data/` folder through `data.dvc`
- A local folder (`s3/`) acts as the DVC remote that stores each version
- `projectflow.txt` lists the commands used, in order

## Project structure
```
Data_versioning_DVC/
├── .dvc/            DVC config and remote setting
├── s3/              Local DVC remote storage
├── data.dvc         Pointer to the tracked data
├── mycode.py        Creates and edits the dataset
├── projectflow.txt  Command steps followed
└── LICENSE          MIT licence
```

## Getting started
Requirements: Python 3.8+, DVC.
```bash
git clone https://github.com/abhijha8287/Data_versioning_DVC.git
cd Data_versioning_DVC
pip install dvc pandas
dvc pull                 # restore data/ from the local remote
python mycode.py         # change the data
dvc add data/ && dvc push
```
Use `git checkout <commit> && dvc checkout` to go back to an earlier data version.

## Tech stack
Python, pandas, DVC

## Notes
MIT licensed.
