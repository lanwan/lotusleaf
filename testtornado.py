import logging

try:
    import tornado
    import tornado.ioloop
    import tornado.web
except:
    logging.error('Load tornado library fail!')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def run():
    application = tornado.web.Application([(r"/", MainHandler),])
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
