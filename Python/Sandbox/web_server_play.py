from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import cgi
import json

my_var = "Lorem ipsum"

main_dict = {}

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self.write_response(b'')

    def do_POST(self):
        content_length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(content_length)
        self.write_response(body)
        request = self.read_response(body)
        print(request)
        d = json.loads(request)
        print(type(request))
        print(type(d))
        print(d['test'])
        #self.check_request(request)
        #self.write_response(main_dict)
    
    def write_response(self, content):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(content)
        #self.wfile.write("test".encode())

        print(self.headers)
        print(content.decode('utf-8'))
    
    def read_response(self, content):
        content_decoded = content.decode('utf-8')
        print('Got the following content: {}'.format(content_decoded))
        return content_decoded
    
    def check_request(self, request_list):
        for item in request_list:
            main_dict[item] = int(len(item))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=80):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()