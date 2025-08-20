# Instructions to Setup VS Code for Python Coding on Mac

## Creating Virtual Environment

Create a Virtual Environment called .venv

.venv is the convention to hide the venv folder

```
python3 -m venv .venv
source .venv/bin/activate
## now set the python interpreter path to the venv's python interpreter by clicking cmd+shift+p and select "Python: Select Interpreter"
```
Other useful commands:
```
## to deactivate the virtual environment
deactivate

which python3
python3 --version
```

## Installing Packages Using Pip
```
pip3 list
pip3 install --upgrade pip
pip3 install pandas
pip3 install ipykernel
## to set the python kernel of jupyter notebook, create a python file, click cmd+enter to bring up the jupyter notebook output, in the top right corner, click Select Kernel. Pick Python (.venv)
```
