fl-t: a command line tool for quick basic flask server generation
=================================================================

To Install
----------

```python
$ python setup.py install
```

To Use
------

```
$ fl-t project_directory_name
```

Doing so will create a project folder for you that is set up for Flask. 

It has a virtualenv (venv) ready to go with basic Flask tools (ex. Jinja) that you can fire up with
```
$ source venv/bin/activate
```

It also includes two template files, a barebones server and a simple folder structure for your project
that meets Flask's structuring needs.

Right now, it is optimized for my set-up, so it creates files in "../Documents/Programming/"
If you would rather set up your base for your projects somewhere else, change the PROJECT_DIRECTORY
variable in fl-t.py as appropriate. 

Currently includes Bootstrap and JQuery CDN links because I like having those handy. 
