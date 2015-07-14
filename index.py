# -*- coding: utf-8 -*-
from bottle import route, run, template
import mpi

@route('/')
def root():
    return template('web')

@route('/motion')
def motion():
    mpi.main()
    return "プログラム起動"

@route('/test')
def test():
    return "test"

run(host='0.0.0.0', port=8080)
