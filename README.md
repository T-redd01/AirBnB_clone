Air bnb clone the console

The console-
Resources:

[Python packages](https://intranet.alxswe.com/concepts/66)
[AirBnB clone](https://intranet.alxswe.com/concepts/74)

[cmd module](https://docs.python.org/3.8/library/cmd.html)
[cmd module in depth](https://pymotw.com/2/cmd/)
[uuid module](https://docs.python.org/3.8/library/uuid.html)
[datetime](https://docs.python.org/3.8/library/datetime.html)
[unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
[args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
[Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
[cmd module wiki page](https://wiki.python.org/moin/CmdModule)
[python unittest](https://realpython.com/python-testing/)



General
How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function


Web Static-
Resources:

[HTML/CSS](https://intranet.alxswe.com/concepts/2)
[The trinity of front-end quality](https://intranet.alxswe.com/concepts/4)

[Learn to Code HTML & CSS (until “Creating Lists” included)](https://learn.shayhowe.com/html-css/)
[Inline Styles in HTML](https://www.codecademy.com/article/html-inline-styles)
[Specifics on CSS Specificity](https://css-tricks.com/specifics-on-css-specificity/)
[CSS SpeciFishity](https://www.standardista.com/cgi-sys/suspendedpage.cgi)
[Introduction to HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML)
[CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)
[MDN](https://developer.mozilla.org/en-US/)
[center boxes](https://css-tricks.com/centering-css-complete-guide/)



General
What is HTML
How to create an HTML page
What is a markup language
What is the DOM
What is an element / tag
What is an attribute
How does the browser load a webpage
What is CSS
How to add style to an element
What is a class
What is a selector
How to compute CSS Specificity Value
What are Box properties in CSS




MySQL-

Environment variables will be your best friend for this project!

HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
HBNB_MYSQL_USER: the username of your MySQL
HBNB_MYSQL_PWD: the password of your MySQL
HBNB_MYSQL_HOST: the hostname of your MySQL
HBNB_MYSQL_DB: the database name of your MySQL
HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)


Resources:

[cmd module](https://docs.python.org/3/library/cmd.html)
[unittest module](https://docs.python.org/3/library/unittest.html#module-unittest)
[args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
[SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
[How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
[Python3 and environment variables](https://docs.python.org/3/library/os.html?highlight=env#os.getenv)
[SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
[MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)



General
What is Unit testing and how to implement it in a large project
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function
How to create a MySQL database
How to create a MySQL user and grant it privileges
What ORM means
How to map a Python Class to a MySQL table
How to handle 2 different storage engines with the same codebase
How to use environment variables



Deploy Static-
Resources:

[CI/CD](https://intranet.alxswe.com/concepts/43)
[AirBnB clone](https://intranet.alxswe.com/concepts/74)

[How to use Fabric](https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments)
[How to use Fabric in Python](https://www.pythonforbeginners.com/systems-programming/how-to-use-fabric-in-python)
[Fabric and command line options](https://docs.fabfile.org/en/1.13/usage/fab.html)
[Nginx configuration for beginners](https://nginx.org/en/docs/beginners_guide.html)
[Difference between root and alias on NGINX](https://blog.heitorsilva.com/en/nginx/diferenca-entre-root-e-alias-do-nginx/)
[Fabric for Python 3](https://github.com/mathiasertl/fabric)
[Fabric Documentation](https://www.fabfile.org/)



General
What is Fabric
How to deploy code to a server easily
What is a tgz archive
How to execute Fabric command locally
How to execute Fabric command remotely
How to transfer files with Fabric
How to manage Nginx configuration
What is the difference between root and alias in a Nginx configuration


Install Software:
Fabric for Python 3 - version 1.14.post1:
$ pip3 uninstall Fabric
$ sudo apt-get install libffi-dev
$ sudo apt-get install libssl-dev
$ sudo apt-get install build-essential
$ sudo apt-get install python3.4-dev
$ sudo apt-get install libpython3-dev
$ pip3 install pyparsing
$ pip3 install appdirs
$ pip3 install setuptools==40.1.0
$ pip3 install cryptography==2.8
$ pip3 install bcrypt==3.1.7
$ pip3 install PyNaCl==1.3.0
$ pip3 install Fabric3==1.14.post1



Web Framework:
Resources:

[What is a Web Framework?](https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb)
[A Minimal Application](https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application)
[Routing (except “HTTP Methods”)](https://flask.palletsprojects.com/en/2.3.x/quickstart/#routing)
[Rendering Templates](https://flask.palletsprojects.com/en/2.3.x/quickstart/#rendering-templates)
[Synopsis](https://jinja.palletsprojects.com/en/2.9.x/templates/#synopsis)
[Variables](https://jinja.palletsprojects.com/en/2.9.x/templates/#variables)
[Comments](https://jinja.palletsprojects.com/en/2.9.x/templates/#comments)
[Whitespace Control](https://jinja.palletsprojects.com/en/2.9.x/templates/#whitespace-control)
[List of Control Structures (read up to “Call”)](https://jinja.palletsprojects.com/en/2.9.x/templates/#list-of-control-structures)
[Flask](https://palletsprojects.com/p/flask/)
[Jinja](https://jinja.palletsprojects.com/en/2.9.x/templates/)

[Playlist for getting started with flask](https://youtu.be/MwZwr5Tvyxo?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)




General
What is a Web Framework
How to build a web framework with Flask
How to define routes in Flask
What is a route
How to handle variables in a route
What is a template
How to create a HTML response in Flask by using a template
How to create a dynamic template (loops, conditions…)
How to display in HTML data from a MySQL database


Install Software:
Flask:
$ pip3 install Flask



RESTful API-

Resources:

[REST API](https://intranet.alxswe.com/concepts/45)
[AirBnB clone](https://intranet.alxswe.com/concepts/74)

[Learn REST: A RESTful Tutorial](https://www.restapitutorial.com/)
[Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
[HTTP access control (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
[Flask cheatsheet](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/301/flask_cheatsheet.pdf)
[What are Flask Blueprints, exactly?](https://stackoverflow.com/questions/24420857/what-are-flask-blueprints-exactly)
[Flask](https://palletsprojects.com/p/flask/)
[Modular Applications with Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
[Flask tests](https://flask.palletsprojects.com/en/1.1.x/testing/)
[Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)



General
What REST means
What API means
What CORS means
What is an API
What is a REST API
What are other type of APIs
Which is the HTTP method to retrieve resource(s)
Which is the HTTP method to create a resource
Which is the HTTP method to update resource
Which is the HTTP method to delete resource
How to request REST API
