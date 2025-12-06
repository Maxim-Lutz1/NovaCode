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
-   ✅ Cross-platform (Linux / Windows / macOS)

------------------------------------------------------------------------

## Requirements

-   Python 3.10+
-   pip
-   Git (optional, for development)
-   (Linux) build-essential (only required for packaging)

------------------------------------------------------------------------

## Installation (Development)

Clone the repository and enter the project directory:

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

## Build

### Build executable with PyInstaller

``` bash
pyinstaller --onefile --windowed src/main.py
```

Resulting binary will be created in:

    dist/

------------------------------------------------------------------------

### Build native binary with Nuitka (faster)

``` bash
python3 -m nuitka --standalone --onefile src/main.py
```

The output binary will appear in the project folder.

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
    └── .venv/        (ignored by git)

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