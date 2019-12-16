# Quick Tips

Here's a few tips and links I found helpful while working on this project. I created this document while I was working on my poject so I could record all the external resources I was accessing and the problems I faced. Hopefully, this could help anyone facing similar issues while trying to replicate this project.

## Creating a Virtual Environment

I used a new virtual environment for this project. Useful when you're using different versions of packages for different projects.
Here's a link on how to get started with those : [Installing and using virtualenv with Python 3](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3)

I ran into problems with the default ExecutionPolicy for .ps1 files on my Windows machine. This [thread](https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system) helped.

## Using Virtual Environments with VS Code

You don't really have to activate/deactivate your virtual environment every time you run your code. All you have to do is change the python interpreter being used by whatever editor you're using. I use VSCode, and found this [nifty little guide on changing environments](https://code.visualstudio.com/docs/python/environments#_where-the-extension-looks-for-environments). If you're using a different editor, you should look for a way to set the current interpreter to the one in your new environment.

## OpenCV2 installation

I used the pre-built binaries from [here](https://pypi.org/project/opencv-python/). Just run the following commmand after you activate your virtual environment
```python
pip install opencv-contrib-python==4.1.0.25
```


