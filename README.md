# NovaCode

NovaCode is a minimal, fast, and hackable code editor built with Python
and PySide6.\
It focuses on simplicity, keyboard-driven workflow, and clean
architecture.

------------------------------------------------------------------------

## Features

-   ✅ GUI editor (Qt / PySide6)
-   ✅ Open files
-   ✅ Save files
-   ✅ Save As
-   ✅ Keyboard shortcuts:
    -   Ctrl+O → Open
    -   Ctrl+S → Save
    -   Ctrl+Shift+S → Save As
    -   Ctrl+Q → Exit
-   ✅ Cross-platform (Linux / Windows)

------------------------------------------------------------------------

## Requirements

-   Python 3.10+
-   pip
-   Git (optional)
-   (Linux) build-essential (only for binary builds)

------------------------------------------------------------------------

## Installation (Development)

Clone the repository:

``` bash
git clone https://github.com/Maxim-Lutz1/NovaCode.git
cd NovaCode
```

Create and activate a virtual environment:

``` bash
python3 -m venv .venv
source .venv/bin/activate     # Linux / macOS
# .venv\Scripts\activate      # Windows
```

Install dependencies:

``` bash
pip install PySide6 pyinstaller nuitka black pylint pytest
```

Run NovaCode:

``` bash
python3 src/main.py
```

------------------------------------------------------------------------

# Building NovaCode

NovaCode can be packaged as a native executable for Windows, Linux and
macOS.

------------------------------------------------------------------------

## Linux Build

### With PyInstaller (recommended first build)

``` bash
pyinstaller --onefile --windowed src/main.py
```

Binary will be located in:

    dist/

------------------------------------------------------------------------

### With Nuitka (faster / native backend)

``` bash
python3 -m nuitka --standalone --onefile src/main.py
```

The resulting binary will appear in the project directory.

------------------------------------------------------------------------

## Windows Build

On Windows, open **PowerShell** or **CMD**, then:

Activate venv:

``` cmd
.venv\Scripts\activate
```

Then build:

``` cmd
pyinstaller --onefile --windowed src\main.py
```

You will get:

    dist\main.exe

Rename it:

    NovaCode.exe

------------------------------------------------------------------------

### Windows (Nuitka -- optional advanced)

``` cmd
python -m nuitka --standalone --onefile src\main.py
```

------------------------------------------------------------------------

## macOS Build

### Requirements:

-   Python 3 (via Homebrew recommended)
-   Xcode Command Line Tools

Install tools:

``` bash
xcode-select --install
```

Activate environment:

``` bash
source .venv/bin/activate
```

Build:

``` bash
pyinstaller --onefile --windowed src/main.py
```

Binary will appear in:

    dist/

------------------------------------------------------------------------

## Output Files

After build:

  OS        Output
  --------- --------------------------
  Linux     `NovaCode`
  Windows   `NovaCode.exe`
  macOS     `NovaCode.app` or binary

------------------------------------------------------------------------

## Project Structure

    NovaCode/
    │
    ├── src/
    │   └── main.py
    │
    ├── VERSION
    ├── README.md
    ├── .gitignore
    └── .venv/        (ignored)

------------------------------------------------------------------------

## Architecture (Conceptual Overview)

    Application (QApplication)
            |
            v
    MainWindow (QMainWindow)
            |
            v
    Editor (QPlainTextEdit)
            |
            v
    Filesystem (Open / Save / Save As)

------------------------------------------------------------------------

## Philosophy

NovaCode is built by using NovaCode.

No unnecessary features.\
No heavy frameworks.\
No complexity for the sake of complexity.

Just a clean editor. Built from real usage.
