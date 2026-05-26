from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "localhost"
PORT = 8080


def handle_message():
    location_lat = "51.5074 N"
    location_long = "-0.1278 W"
    strike_lat = "50.2134 N"
    strike_long = "1.5943 W"
    strike_time = "01h45m53s"
    strike_distance = "32 miles"

    return f"Your location: {location_lat}, {location_long}\nLightning Strike: {strike_lat}, {strike_long}\nDistance: {strike_distance}\nTime since strike: {strike_time}"


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = handle_message()

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))


def main():
    server = HTTPServer((HOST, PORT), RequestHandler)
    print(f"Server running at http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()
