import os
import http.server
import socketserver

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # self.send_response(HTTPStatus.OK)
        # self.end_headers()
        self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
        # msg = 'Hello me and you! you requested %s' % (self.path)
        # self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
