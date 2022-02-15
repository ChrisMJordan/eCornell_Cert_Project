"""
The script code for the application.

This file should be kept simple.  If written correctly, it will have no more than
three lines of code (most of those imports).  It should call the execute() function
in module app.py, passing it the contents of sys.argv EXCEPT for the application name
(so only the command line arguments AFTER 'python auditor').

Author: Christopher Jordan
Date: September 30, 2021
"""
import app
import sys

arguments = sys.argv[1:]
app.execute(*arguments)
