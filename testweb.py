import logging
import os


try:
    import tornado
    import tornado.ioloop
    import tornado.web
except:
    logging.error('Load tornado library fail!')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello, world")
        items = ["Item 1", "Item 2", "Item 3"]
        path = os.path.join(os.getcwd(), "//static//test.html")
        print path
        self.render(path, title="My title", items=items)


def run():
    application = tornado.web.Application([(r"/", MainHandler),])
    application.listen(8000)    
    tornado.ioloop.IOLoop.instance().start()