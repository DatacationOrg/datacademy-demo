# Datacademy Demo

The Datacademy, presented by Datacation B.V., provides this repository containing various exercises designed to enhance your Data Science skills. 
As you will notice, the modules listed above or on the left side correspond to the theoretical segments found in Easy-LMS. 
Upon completing a theoretical section in Easy-LMS, you'll be prompted to access the relevant files in this repository. 
The exercises in most modules are conducted using Notebooks, whose format conveniently allows for text to be interspersed between code cells, guiding you through each exercise.

As you progress, however, you will encounter later modules that predominantly use plain Python files. This is because some required functionalities are not compatible with Notebooks. Having gained some experience in coding, we anticipate that you will adapt to this change without significant difficulty. Additionally, working with plain Python files is a common practice in the field, and this experience will be valuable for your professional development.

We wish you not only success but also a great deal of enjoyment as you take your first steps on your data journey!

Best regards, Team Datacademy.

## Installation instructions

### Step 0. Install Python (optional)
The Datacademy supports **Python version 3.10 and higher**. If you do not have Python installed, you can simply do so from the [Python website](https://www.python.org/downloads/).

### Step 1. Install and set up the package manager
1. Open this folder in [VS Code](https://code.visualstudio.com/).
2. Open a terminal and execute the following commands:

```bash
# Install/update package manager
python -m pip install --upgrade pip
python -m pip install --upgrade poetry

# Let poetry create a virtual environment
python -m poetry config virtualenvs.create true
python -m poetry config virtualenvs.in-project true
```

### Step 2. Install dependencies
Execute the following commands to install all necessary packages. We call this the dependencies. 

```bash
# This install all dependencies.
python -m poetry install --no-root
```

You should now have a folder called `.venv`. It might not show in your editor, but you can see it in file explorer. These dependencies are specified in `pyproject.toml`, but you don't need to worry about that!

### Step 3. Select the environment as interpreter
In VS Code, use `ctrl+shift+p` and then use `Python: Select Interpreter` to select the virtual environment in `.venv` as the python interpreter. The correct interpreter should look something like:

> Python 3.11.5 ('.venv': Poetry) `.\venv\Scripts\python.exe`

In Notebooks, also select this interpreter at the top right.

**Now, you are good to go!**
