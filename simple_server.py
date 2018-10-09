import http.server

server_address = ("", 8000)
#ハンドラを設定
handler_class = http.server.SimpleHTTPRequestHandler
#handler_class = http.server.CGIHTTPRequestHandler
simple_server = http.server.HTTPServer(server_address, handler_class)
simple_server.serve_forever()