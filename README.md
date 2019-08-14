# A program for tagging git repository

* Will create a git tag containing the current time and date.
* If the current branch is not master will create another git tag containing the
name of the current branch. 
_(Github doesn't allow to tag with the name of the branch, it says that the rag already exists.  That is why I added 'tag' in front of the branch name)._
* If supplied with an optional parameter will also create a git tag containing the
value of that parameter.
* Will push all created tags to `origin`.

## Running as a standalone executable script

For mac:
```
./tagging-mac [param1]
```

For windows:
```
tagging-win.exe [param1]
```

For linux:
```
./tagging-linux [param1]
```


## Running the python script

#### REQUIREMENTS
GitPython needs the git executable to be installed on the system and available in your PATH for most operations. 
Git (1.7.x or newer)
Python 3 to 3.7.
The list of dependencies are listed in ./requirements.txt. The installer takes care of installing them for you.

#### INSTALL dependencies

```
python setup.py install
```
or 

```
pip install GitPython
```

#### RUNNING THE PYTHON SCRIPT

```
python tagging.py [tag-param1]
```