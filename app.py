#!/usr/bin/env python

import logging
import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import uuid
import tornado.httpserver

from tornado.options import define, options

import settings as app_settings

define("port", default=app_settings.PORT, help="run on the given port", type=int)



import views.web


import sys



class Application(tornado.web.Application):
    def __init__(self):

        handlers = [         
            
            # MINISITE VIEWS
            #(r"/api/%s/minisite/issues.(json|js)" % api.API_VERSION(), api.MinisiteIssues),
            (r"/(.*)", views.web.Page),
            (r"/", views.web.MainIndex),
            
        ]
        settings = dict(
            cookie_secret="43oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url="/auth/login",
            template_path=os.path.join(os.path.dirname(__file__), "media/tmpl"),
            static_path=os.path.join(os.path.dirname(__file__), "media/static"),
            
            xsrf_cookies=True,
            autoescape=None
        )
        
        tornado.web.Application.__init__(self, handlers, **settings)
        
        




def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()        
    
