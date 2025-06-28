#!/usr/bin/env python3

import os
import sys
import subprocess
import platform
import ast
from pathlib import Path
from shutil import which
import sysconfig

def is_python_installed():
    return which("python") or which("python3")

def get_pip_command():
    for cmd in ("pip", "pip3", f"{sys.executable} -m pip"):
        try:
            subprocess.run(f"{cmd} --version", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return cmd
        except subprocess.CalledProcessError:
            continue
    return None

def extract_imports_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        try:
            tree = ast.parse(file.read(), filename=str(filepath))
        except SyntaxError:
            return set()

    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for n in node.names:
                imports.add(n.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split('.')[0])
    return imports

def get_standard_lib_modules():
    stdlib = sysconfig.get_paths()["stdlib"]
    return {mod.name for mod in Path(stdlib).iterdir() if mod.is_dir() or mod.suffix == '.py'}

def build_requirements(project_dir):
    all_imports = set()
    for py_file in Path(project_dir).rglob("*.py"):
        if "venv" in py_file.parts or "__pycache__" in py_file.parts:
            continue
        all_imports.update(extract_imports_from_file(py_file))

    std_libs = get_standard_lib_modules()
    third_party = sorted(all_imports - std_libs - {"__future__", "typing", "dataclasses"})
    return third_party

def write_requirements_file(modules, path="requirements.txt"):
    if not modules:
        print("✅ No third-party packages detected.")
        return
    with open(path, "w") as f:
        for mod in modules:
            f.write(mod + "\n")
    print(f"📝 Generated {path} with {len(modules)} packages.")

def install_requirements(pip_cmd):
    if not Path("requirements.txt").exists():
        print("⚠️  requirements.txt not found.")
        return
    print("📦 Installing dependencies from requirements.txt ...")
    subprocess.check_call(f"{pip_cmd} install -r requirements.txt", shell=True)

def main():
    print(f"🖥️  OS Detected: {platform.system()}")

    if not is_python_installed():
        print("❌ Python is not installed.")
        print("🔗 Please install Python from https://www.python.org/downloads/ and re-run this script.")
        sys.exit(1)

    print(f"✅ Python is installed at: {sys.executable}")

    pip_cmd = get_pip_command()
    if not pip_cmd:
        print("❌ pip is not available.")
        print("📦 Attempting to install pip ...")
        try:
            subprocess.check_call(f"{sys.executable} -m ensurepip --upgrade", shell=True)
            pip_cmd = get_pip_command()
        except subprocess.CalledProcessError:
            print("❌ Failed to install pip. Please install it manually.")
            sys.exit(1)

    print("🔍 Scanning project for dependencies ...")
    third_party_modules = build_requirements(".")
    write_requirements_file(third_party_modules)
    install_requirements(pip_cmd)
    print("✅ Environment setup complete.")

if __name__ == "__main__":
    main()
