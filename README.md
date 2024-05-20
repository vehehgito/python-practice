# python-practice

## Purpose of this repository
Repository for storing programs from my practice with Python. All the resources used to learn will be stored in the Resources folder.

## Python Command Line
Python Command Line invokation exists with the format:

`
python [-c command | -m module-name | script | - ] [args]
`


## Package Installer for Python (PIP) Commands 
### Installing Package Installer for Python (PIP)
```
python -m ensurepip --upgrade
```

### Upgrading PIP
```
pip install --upgrade pip
```

### Creating a virtual environment for dependencies (Python 3.4 and above)
```
python -m venv venv
```

### Creating a requirements.txt file
```
pip freeze > requirements.txt
```

### Installing dependencies from the requirements.txt file
```
pip install -r requirements.txt
```

### Disabling building dependencies from .WHL files
```
pip install --no-binary ModuleName
```

### Listing installed dependencies
```
pip list
```

### Searching for a package
```
pip search "ModuleName"
```

### Setting up command completion for PowerShell
```
python -m pip completion --powershell | Out-File -Encoding default -Append $PROFILE
```

### Upgrading dependencies which need an upgrade
```
pip install --upgrade SomePackage --upgrade-strategy=only-if-needed
```

## Virtual Environment Commands

### Activating the virtual environment
#### In cmd.exe
```
venv\Scripts\activate.bat
```

#### In PowerShell
```
venv\Scripts\Activate.ps1
```

