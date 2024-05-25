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

### Install options
| **Options** | **Function** |
|---|---|
| `-r, --requirement <file>`               | Install from the given requirements file. This option can be used multiple times.                                                                                                                                       |
| `-c, --constraint <file>`                | Constrain versions using the given constraints file. This option can be used multiple times.                                                                                                                             |
| `--no-deps`                              | Don’t install package dependencies.                                                                                                                                                                                     |
| `--pre`                                  | Include pre-release and development versions. By default, pip only finds stable versions.                                                                                                                                |
| `-e, --editable <path/url>`              | Install a project in editable mode (i.e. setuptools “develop mode”) from a local project path or a VCS url.                                                                                                              |
| `--dry-run`                              | Don’t actually install anything, just print what would be. Can be used in combination with --ignore-installed to ‘resolve’ the requirements.                                                                             |
| `-t, --target <dir>`                     | Install packages into `<dir>`. By default this will not replace existing files/folders in `<dir>`. Use --upgrade to replace existing packages in `<dir>` with new versions.                                               |
| `--platform <platform>`                  | Only use wheels compatible with `<platform>`. Defaults to the platform of the running system. Use this option multiple times to specify multiple platforms supported by the target interpreter.                          |
| `--python-version <python_version>`      | The Python interpreter version to use for wheel and “Requires-Python” compatibility checks. Defaults to a version derived from the running interpreter.                                                                 |
| `--implementation <implementation>`      | Only use wheels compatible with Python implementation `<implementation>`, e.g. ‘pp’, ‘jy’, ‘cp’, or ‘ip’. If not specified, then the current interpreter implementation is used. Use ‘py’ to force implementation-agnostic wheels. |
| `--abi <abi>`                            | Only use wheels compatible with Python abi `<abi>`, e.g. ‘pypy_41’. If not specified, then the current interpreter abi tag is used. Use this option multiple times to specify multiple abis supported by the target interpreter. |
| `--user`                                 | Install to the Python user install directory for your platform. Typically `~/.local/`, or `%APPDATA%Python` on Windows. (See the Python documentation for site.USER_BASE for full details.)                               |
| `--root <dir>`                           | Install everything relative to this alternate root directory.                                                                                                                                                            |
| `--prefix <dir>`                         | Installation prefix where lib, bin and other top-level folders are placed. Note that the resulting installation may contain scripts and other resources which reference the Python interpreter of pip, and not that of --prefix. |
| `--src <dir>`                            | Directory to check out editable projects into. The default in a virtualenv is `<venv path>/src`. The default for global installs is `<current dir>/src`.                                                                  |
| `-U, --upgrade`                          | Upgrade all specified packages to the newest available version. The handling of dependencies depends on the upgrade-strategy used.                                                                                       |
| `--upgrade-strategy <upgrade_strategy>`  | Determines how dependency upgrading should be handled [default: only-if-needed]. “eager” - dependencies are upgraded regardless of whether the currently installed version satisfies the requirements of the upgraded package(s). |
| `--force-reinstall`                      | Reinstall all packages even if they are already up-to-date.                                                                                                                                                              |
| `-I, --ignore-installed`                 | Ignore the installed packages, overwriting them. This can break your system if the existing package is of a different version or was installed with a different package manager!                                           |
| `--ignore-requires-python`               | Ignore the Requires-Python information.                                                                                                                                                                                  |
| `--no-build-isolation`                   | Disable isolation when building a modern source distribution. Build dependencies specified by PEP 518 must be already installed if this option is used.                                                                  |
| `--use-pep517`                           | Use PEP 517 for building source distributions (use --no-use-pep517 to force legacy behaviour).                                                                                                                           |
| `--check-build-dependencies`             | Check the build dependencies when PEP517 is used.                                                                                                                                                                        |
| `--break-system-packages`                | Allow pip to modify an EXTERNALLY-MANAGED Python installation.                                                                                                                                                           |
| `-C, --config-settings <settings>`       | Configuration settings to be passed to the PEP 517 build backend. Settings take the form KEY=VALUE. Use multiple --config-settings options to pass multiple keys to the backend.                                          |
| `--global-option <options>`              | Extra global options to be supplied to the setup.py call before the install or bdist_wheel command.                                                                                                                      |
| `--compile`                              | Compile Python source files to bytecode.                                                                                                                                                                                 |
| `--no-compile`                           | Do not compile Python source files to bytecode.                                                                                                                                                                          |
| `--no-warn-script-location`              | Do not warn when installing scripts outside PATH.                                                                                                                                                                        |
| `--no-warn-conflicts`                    | Do not warn about broken dependencies.                                                                                                                                                                                   |
| `--no-binary <format_control>`           | Do not use binary packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either “:all:” to disable all binary packages, “:none:” to empty the set, or one or more package names with commas between them. |
| `--only-binary <format_control>`         | Do not use source packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either “:all:” to disable all source packages, “:none:” to empty the set, or one or more package names with commas between them. |
| `--prefer-binary`                        | Prefer binary packages over source packages, even if the source packages are newer.                                                                                                                                      |
| `--require-hashes`                       | Require a hash to check each requirement against, for repeatable installs. This option is implied when any package in a requirements file has a --hash option.                                                           |
| `--progress-bar <progress_bar>`          | Specify whether the progress bar should be used [on, off] (default: on).                                                                                                                                                 |
| `--root-user-action <root_user_action>`  | Action if pip is run as a root user. By default, a warning message is shown.                                                                                                                                             |
| `--report <file>`                        | Generate a JSON file describing what pip did to install the provided requirements. Can be used in combination with --dry-run and --ignore-installed to ‘resolve’ the requirements. When - is used as file name it writes to stdout. |
| `--no-clean`                             | Don’t clean up build directories.                                                                                                                                                                                        |
| `-i, --index-url <url>`                  | Base URL of the Python Package Index (default https://pypi.org/simple). This should point to a repository compliant with PEP 503 (the simple repository API) or a local directory laid out in the same format.             |
| `--extra-index-url <url>`                | Extra URLs of package indexes to use in addition to --index-url. Should follow the same rules as --index-url.                                                                                                            |
| `--no-index`                             | Ignore package index (only looking at --find-links URLs instead).                                                                                                                                                        |
| `-f, --find-links <url>`                 | If a URL or path to an html file, then parse for links to archives such as sdist (.tar.gz) or wheel (.whl) files. If a local path or file:// URL that’s a directory, then look for archives in the directory listing. Links to VCS project URLs are not supported. |


## Virtual Environment Commands
### Creating a virtual environment for dependencies (Python 3.4 and above)
```
python -m venv venv
```

### Activating the virtual environment
#### In cmd.exe
```
venv\Scripts\activate.bat
```

#### In PowerShell
```
venv\Scripts\Activate.ps1
```