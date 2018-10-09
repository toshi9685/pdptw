#!/usr/bin/env python3
# coding: utf-8

import cgi
from datetime import datetime

html_body = """
<html>
    <head>
         <meta http-equiv="content-type"content="text/html;charset=utf-8">
    </head>
    <body>
        foo = %s
    </body>
</html>"""
import cgi
form=cgi.FieldStorage()
print("Content-type: text/html\n")
print(html_body % form.getvalue('foo', 'N/A'))