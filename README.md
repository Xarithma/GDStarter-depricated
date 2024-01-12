# ~~GDStarter~~ We are moving back to using a plugin to manage this instead.

The simple Godot CLI tool to start your project with the right boilerplate.

## Quickstart

While not required, I highly recommend creating a virtual environment before
installing this package:

```bash
python3 -m venv venv

# Linux/macOS
source ./venv/bin/activate

# Windows
.\venv\Scripts\activate
```

Install the package:

```
pip install gdstarter
```

Run the script (interactive):

```
gdstarter
```

If you don't want to use the interactive project creation run the script with
the `--help` argument:

```
gdstarter --help

usage: gdstarter [-h] [--name NAME] [--features [FEATURES ...]] [--template TEMPLATE]

A simple tool to start Godot projects.

options:
  -h, --help            show this help message and exit
  --name NAME           Specify project name
  --features [FEATURES ...]
                        Specify project features
  --template TEMPLATE   Specify project template
```
