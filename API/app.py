from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {'message': 'Hello, World!'}
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {'message': 'Not Found'}
            self.wfile.write(json.dumps(data).encode())

def run_server():
    host = 'localhost'
    port = 8080
    server_address = (host, port)

    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Server running at http://{host}:{port}/')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Server stopped.')
        httpd.server_close()

if __name__ == '__main__':
    run_server()