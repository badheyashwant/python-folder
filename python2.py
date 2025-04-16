import tornado.ioloop
import tornado.web
import tornado.httpclient
import asyncio

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Welcome to Tornado Home Page!")

class ApiHandler(tornado.web.RequestHandler):
    async def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        response = await client.fetch("https://api.github.com")
        self.write(response.body)

def make_app():
    return tornado.web.Application([
        (r"/", HomeHandler),
        (r"/api", ApiHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    print("Server running on http://localhost:8000")
    tornado.ioloop.IOLoop.current().start()


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Welcome to Tornado Home Page!")

class ApiHandler(tornado.web.RequestHandler):
    async def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        response = await client.fetch("https://api.github.com")
        self.write(response.body)

def make_app():
    return tornado.web.Application([
        (r"/", HomeHandler),
        (r"/api", ApiHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    print("Server running on http://localhost:8000")
    tornado.ioloop.IOLoop.current().start()