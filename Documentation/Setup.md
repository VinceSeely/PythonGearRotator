# Libraries

## TKinter

if using anaconda:
```conda install -c anaconda tk```

## Build Executable

### Install Pyinstaller 

#### Using Anaconda

```
conda install -c conda-forge pyinstaller
```
```
conda install -c anaconda pywin3
```

#### Using PIP

```
pip install pyinstaller
```

### Creating Windows Executable

```
pyinstaller .\GUI.spec
```

the executable will be stored in ```.\dist\GUI.exe``` after running the above line. 
To build on MAC OS run ```pyinstaller --onefile .\src\GUI.py