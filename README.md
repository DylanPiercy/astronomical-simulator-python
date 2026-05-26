# Astronomical Simulator Python

> **A revisited version of an earlier project, rebuilt in Python to simulate a solar system using physics-based calculations and 3D rendering with VPython.**

---

## 📋 Table of Contents

- [Astronomical Simulator Python](#astronomical-simulator-python
    - [Table of Contents](#-table-of-contents)
    - [Project Setup](#project-setup)
        - [Prerequisites](#prerequisites)
        - [Setup Virtual Environment](#setup-virtual-environment)
    - [Git Commit Types](#git-commit-types)
    - [Known Bugs](#known-bugs)

---

## Project Setup

### Prerequisites

- **Python 3.12+** installed on your system.
- **Internet connection** for downloading dependencies.

---

### Setup Virtual Environment

#### Step 1: Create the virtual environment

```bash
python3 -m venv astro_env
```

#### Step 2: Activate the virtual environment

**🐧 Linux / MacOS:**

```bash
source astro_env/bin/activate
```

**🪟 Windows:**

```bash
# CMD
astro_env\Scripts\activate

# PowerShell
astro_env/Scripts/Activate.ps1
```

#### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

> **💡 Tip:** To deactivate the virtual environment later, simply run `deactivate`

---




---

## Git Commit Types

| Type       | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| `build`    | Changes that affect the **build** or external dependencies.                 |
| `docs`     | Changes to **documentation** and **comments**.                              |
| `feat`     | Introduces or changes a **feature** of the project.                         |
| `fix`      | Fixes a **bug** or unintended behavior.                                     |
| `git`      | Changes to **Git settings**.                                                |
| `merge`    | Merge of git branches.                                                      |
| `perf`     | Improves **performance** of the codebase.                                   |
| `refactor` | **Code restructuring** without changing behavior or adding features.        |
| `revert`   | Reverts a previous commit.                                                  |
| `format`   | Changes that **don’t affect logic**, like formatting or spacing.            |
| `struct`   | Changes to **project structure** (e.g., file reorganisation).               |
| `test`     | Adds or updates codebase **tests**.                                         |
| `temp`     | A **temporary** change to the code.                                         |

---

## Known Bugs

- The simulation speed slider displays an inaccurate “simulated days per second” value while it is being dragged. The displayed value is usually off by ±1, but can be further out during fast or large slider movements. Once the slider is released, the correct value is displayed.

---
