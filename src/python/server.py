from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from functions.movie_data import users, ratings, movies
from functions.recommendation import recommend_movie
from functions.item_based import item_based_recommendation

hostname = "localhost"
serverPort = 8080

class DataHandlerServer(BaseHTTPRequestHandler):
  def do_GET(self):
        if self.path == '/get-users':
          self.send_response(200)
          self.send_header('Content-type','text/html')
          self.end_headers()
          users_json = json.dumps(users)
          self.wfile.write(bytes(users_json, "utf-8"))
        elif self.path == '/get-movies':
          self.send_response(200)
          self.send_header('Content-type','text/html')
          self.end_headers()
          movies_json = json.dumps(movies)
          self.wfile.write(bytes(movies_json, "utf-8"))
        else:
          self.send_response(200)
          self.send_header('Content-type','text/html')
          self.end_headers()
          self.wfile.write(bytes("Welcome!", "utf8"))
  def do_POST(self):
    if self.path == '/get-rec':
      self.send_response(200)
      content_length = int(self.headers['Content-Length'])
      raw_data = self.rfile.read(content_length)
      data = json.loads(raw_data.decode('utf-8'))
      if(data['rectype'] == "moviebased"):
        recommendations = recommend_movie(ratings, int(data['user']), data['method'])
      else :
        recommendations = item_based_recommendation(ratings, int(data['user']))
      recommendations_json = json.dumps(recommendations)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      self.wfile.write(bytes(recommendations_json, "utf8"))
    else:
      self.send_response(404)

with HTTPServer((hostname, serverPort), DataHandlerServer) as server:
  print(f'Starting server on port {serverPort}')
  server.serve_forever()