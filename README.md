# EX01 Developing a Simple Webserver
## Date: 09.04.2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
    <body bgcolor="PINK">
        <table border="5" cellpadding="22" align="center" bgcolor="cyan">
            <caption align="center">SMARTPHONE CONFIGURATION</caption>
        
            <tr bgcolor="blue">
                <th>S.NO</th><th>CONFIGURATION</th><th>DETAILS</th>
            </tr>
            <tr>
                <td>1</td><td>PROCESSOR</td><td>Snapdragon 888</td>
            </tr>
            <tr>
                <td>2</td><td>RAM</td><td>8GB</td>
            </tr>
            <tr>
                <td>3</td><td>STORAGE</td><td>128 GB</td>
            </tr>
            <tr>
                <td>4</td><td>OS</td><td>Android 12</td>
            </tr>
            <tr>
                <td>5</td><td>CAMERA</td><td>64MP</td>
            </tr>
            <tr>
                <td>6</td><td>BATTERY</td><td>4000mAh</td>
            </tr>
        </table>
    </body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:

NAME           : S KANUSHA SREE
REGISTER NUMBER: 212224040149

![alt text](<Screenshot 2025-05-11 174249.png>)

![alt text](<Screenshot 2025-05-12 102853.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
