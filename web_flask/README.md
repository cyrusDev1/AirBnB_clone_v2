0x04. AirBnB clone - Web framework
==================================

PythonBack-endWebserverFlask

-   By: Guillaume, CTO at Holberton School
-   Weight: 2
-   Project will start Oct 13, 2022 4:00 AM, must end by Oct 17, 2022 4:00 AM
-   will be released at Oct 14, 2022 4:00 AM
-   **Manual QA review must be done** (request it when you are done with the project)
-   An auto review will be launched at the deadline

### Concepts

*For this project, we expect you to look at this concept:*

-   [AirBnB clone](https://alx-intranet.hbtn.io/concepts/74)

Resources
---------

**Read or watch**:

-   [What is a Web Framework?](https://alx-intranet.hbtn.io/rltoken/64SQpOGx46Ljp0zFJchESg "What is a Web Framework?")
-   [A Minimal Application](https://alx-intranet.hbtn.io/rltoken/LM0zyaIOfusNXz12bZXKVQ "A Minimal Application")
-   [Routing](https://alx-intranet.hbtn.io/rltoken/PBYpb5Giu7U5uOb-A9PMxw "Routing") (*except "HTTP Methods"*)
-   [Rendering Templates](https://alx-intranet.hbtn.io/rltoken/g-W9H6gxHkNqaTw6giSG8Q "Rendering Templates")
-   [Synopsis](https://alx-intranet.hbtn.io/rltoken/5Y_A7XB9Qo1JeZgiSUq0yQ "Synopsis")
-   [Variables](https://alx-intranet.hbtn.io/rltoken/ITzobwYP1Lc4KqEUUcYCGw "Variables")
-   [Comments](https://alx-intranet.hbtn.io/rltoken/ykUFuQSE9KD1M7WGY-4v4w "Comments")
-   [Whitespace Control](https://alx-intranet.hbtn.io/rltoken/NMLZom50ZVOxQlgYW3rnuQ "Whitespace Control")
-   [List of Control Structures](https://alx-intranet.hbtn.io/rltoken/5AGhzIt0zSpPJh9SFysdMQ "List of Control Structures") (*read up to "Call"*)
-   [Flask](https://alx-intranet.hbtn.io/rltoken/VJs151_hsE9g7Cw-Pz5bVg "Flask")
-   [Jinja](https://alx-intranet.hbtn.io/rltoken/2y_hunzGCCvSot06EW67UQ "Jinja")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/fja4_zmJuVaRtHFviyVv9Q "explain to anyone"), **without the help of Google**:

### General

-   What is a Web Framework
-   How to build a web framework with Flask
-   How to define routes in Flask
-   What is a route
-   How to handle variables in a route
-   What is a template
-   How to create a HTML response in Flask by using a template
-   How to create a dynamic template (loops, conditions...)
-   How to display in HTML data from a MySQL database

### Copyright - Plagiarism

-   You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
-   You will not be able to meet the objectives of this or any following project by copying and pasting someone else's work.
-   You are not allowed to publish any content of this project.
-   Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
------------

### Python Scripts

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the `PEP 8` style (version 1.7)
-   All your files must be executable
-   The length of your files will be tested using `wc`
-   All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)

### HTML/CSS Files

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files should end with a new line
-   A `README.md` file at the root of the folder of the project is mandatory
-   Your code should be W3C compliant and validate with [W3C-Validator](https://alx-intranet.hbtn.io/rltoken/hsGaWK6aDNB7ax-gkZHfpw "W3C-Validator") (except for jinja template)
-   All your CSS files should be in the `styles` folder
-   All your images should be in the `images` folder
-   You are not allowed to use `!important` or `id` (`#...` in the CSS file)
-   All tags must be in uppercase
-   Current screenshots have been done on `Chrome 56.0.2924.87`.
-   No cross browsers

More Info
---------

### Install Flask

```
$ pip3 install Flask

```

![](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step3.png)