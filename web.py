from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol Suite</title>
</head>
<body bgcolor="PINK">
    <h1 align="center">LIST OF PROTOCOLS IN TCP/IP PROTOCOL SUITE</h1>
    <table border="5" cellpadding="15" align="center" bgcolor="lightblue">
        <tr><th>Layer</th><th>Protocols</th></tr>
        <tr><td>Application Layer</td><td>HTTP, FTP, SMTP, DNS, Telnet, POP3</td></tr>
        <tr><td>Transport Layer</td><td>TCP, UDP</td></tr>
        <tr><td>Internet Layer</td><td>IP, ICMP, IGMP, ARP, RARP</td></tr>
        <tr><td>Network Access Layer</td><td>Ethernet, Wi-Fi, PPP</td></tr>
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