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