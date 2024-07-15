from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but some modules need help.
build_exe_options = {
    "packages": ["os", "pandas", "tabula"],
    "excludes": ["tkinter"],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "PDF Table Extractor",
    version = "0.1",
    description = "Extract tables from PDF and save them to an Excel file",
    options = {"build_exe": build_exe_options},
    executables = [Executable("extract_pdf_tables.py", base=base)]
)
