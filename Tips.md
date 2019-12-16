# Helpful Information

Here's a few tips and links I found helpful while working on this project.

## Using Virtual Environments

I used a new virtual environment for this project. Useful when you're using different versions of packages for different projects.

Here's a link on how to get started with those : [Installing and using virtualenv with Python 3](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3)

I ran into problems with the default ExecutionPolicy for .ps1 files on my Windows machine. This [thread](https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system) helped.

## OpenCV2 installation

I used the pre-built binaries from [here](https://pypi.org/project/opencv-python/). Just run the following commmand after you activate your virtual environment
```python
pip install opencv-contrib-python==4.1.0.25
```

