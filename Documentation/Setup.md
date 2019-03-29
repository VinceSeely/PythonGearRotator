# Libraries

## TKinter

if using anaconda:
```conda install -c anaconda tk```

## Build Executable

### Using Anaconda

isntall Pyinstaller 
```
conda install -c conda-forge pyinstaller
conda install -c anaconda pywin32
```

### Using PIP

```
pip install pyinstaller
```

### Creating Windows Executable

```
pyinstaller --onefile .\src\GUI.py
```

the executable will be stored in ```.\dist\GUI.exe``` after running the above line