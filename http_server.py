from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

from screen_controller import ScreenController


class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = parse_qs(self.rfile.read(content_length).decode())
        action_data = post_data.get('action')
        if action_data and len(action_data) == 1:
            action = action_data[0]
            try:
                screen_action = ScreenController.Action(action)
            except ValueError:
                pass
            else:
                ScreenController.handle_action(screen_action)

        self._set_headers()


def run_server(address='localhost', port=8000):
    server_address = (address, port)
    httpd = HTTPServer(server_address, Handler)

    print(f"Starting httpd server on {address}:{port}")
    httpd.serve_forever()
