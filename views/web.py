
import logging
import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import uuid
import tornado.httpserver
import sys
import random
import json
import re

from Cheetah.Template import Template


from tornado.options import define, options

import settings as settings

class DefaultHandler(tornado.web.RequestHandler):
    
    def render(self, template_name, config_arg={}, **kwargs):
        
              
        config_arg.update({
            # 'BASE_URL': settings.BASE_URL, 
            # 'ASSET_URL': settings.ASSET_URL,   
            'ROOT_URL': settings.BASE_URL 
        })
            
        kwargs.update(config_arg)
                
        compiler_settings = { }
        
         # always include a random number so we can avoid JS caching.
        config_arg['random_number'] = random.randint(0, 1000)
                        
        config_arg['active_page'] = template_name
                        
        template = Template(
            file="media/tmpl/%s.py" % template_name,
            searchList=[config_arg], 
            compilerSettings = compiler_settings)
        result = str(template)
                
        self.write(result)
            
        result = ''
        return        

class MainIndex(DefaultHandler):

    def get(self):
        
        return self.render('index')
        
        
        
class Page(DefaultHandler):
    def get(self, basename=''):   
        
        self.render(is_supported_page(basename), {'foo': 'bar'})
        
        return
        
            
def is_supported_page(basename):
    pages = supported_pages()
    
    for page in pages:
        if (basename == page):
            return page
    
    return 'index'
    
def supported_pages():
    return [
        'map',
        'contact',
        'rsvp',
        'index',
        'accommodations'
    ]
            
