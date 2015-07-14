# -*- coding: utf-8 -*-
from bottle import route, run, template
import motion

@route('/')
def root():
    return template('web')

@route('/motion')
def motion():
    print "aaaaaaaaaaaaaaaaaaaa"
    return template('web')

@route('/test')
def test():
    return "test"


run(host='localhost', port=8080)
