import http.server
import socketserver
import json


class HardwareidServer(http.server.CGIHTTPRequestHandler):

		def do_POST(self):
				content_len = int(self.headers.get('content-length', 0))
				post_body = self.rfile.read(content_len)
				json_body = json.loads(post_body)
				print(json_body)

		def do_GET(self):
				print("in do_get")


PORT = 3000


with socketserver.TCPServer(("", PORT), HardwareidServer) as httpd:
		print("serving at port", PORT)
		httpd.serve_forever()
