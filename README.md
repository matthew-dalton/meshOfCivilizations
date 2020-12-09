# meshOfCivilizations

## Environment Setup

To set up the python virtual environment required to execute this code, run the following in your terminal:

```
git clone https://github.com/matthew-dalton/bias-network.git
cd bias-network
python3 -m virtualenv venv
source venv/bin/activate
pip install < requirements.txt
```

After doing the above, you have the proper virtual environment setup!

If you wish to exit the virtual environment, run the following in your terminal:

```
deactivate
```

When adding to the project, if you need to add another library `<library>` to the project, run the following in your terminal while the virtual environment is activated:

```
pip install <library>
pip freeze > requirements.txt
```
