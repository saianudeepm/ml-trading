# 1. Using Virtualenv

### Install virtualenv
```pip install virtualenv```

### Create a virtual env 
```virtualenv venv --distribute```

### Switch to env
```source venv/bin/activate```
 
### Option1> Workaround to launching python as a framework in virtualenv
reference: [working with matplotlib in MacOSX](https://matplotlib.org/faq/osx_framework.html#working-with-matplotlib-on-osx)

* Switch to the virtualenv
* Add the below function to .bashrc
* Source it and then use this function (frameworkpython) to launch python 

```
function frameworkpython {
    if [[ ! -z "$VIRTUAL_ENV" ]]; then
        PYTHONHOME=$VIRTUAL_ENV /usr/bin/python "$@"
    else
        /usr/bin/python "$@"
    fi
}

export PATH=$PATH:~/.virtualenv
```
### Option2> Workaround for macosx in virtual env by setting backend (preferred)
```
   workon <envName>
   echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc
```


# 2. Using VirtualEnvWrapper 

### Installing virtualenvwrapper
```sudo pip install virtualenvwrapper --ignore-installed six```

### Configuring virtualenvwrapper
```
   export WORKON_HOME=~/Envs
   mkdir -p $WORKON_HOME
   source /usr/local/bin/virtualenvwrapper.sh
   mkvirtualenv env1
```

### Add workon to .bashrc or .bash_profile
```
   echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bash_profile
   source ~/.bash_profile
```

### Switch to an environment using virtualenvwrapper
```
    workon <envName>
```

### Workaround for using matplotlib in macosx virtual env by setting backend
```
   workon <envName>
   echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc
```
