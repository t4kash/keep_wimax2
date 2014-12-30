#!/usr/bin/python
# coding: utf-8
import base64
import mechanize
import logging
from urllib2 import HTTPError


AUTH_ID = 'admin'
AUTH_PASSWORD = 'admin'


def main():
    logging.basicConfig(level=logging.INFO)

    br = mechanize.Browser()
    br.add_password('http://192.168.0.1', AUTH_ID, AUTH_PASSWORD)
    response = br.open('http://192.168.0.1/index.cgi/index_contents')
    # try:
    # except HTTPError, e:
    #     logging.warn('%d: %s' % (e.code, e.msg))
    #     return

    if 'インターネット利用可能(WiMAX)' in response.read():
        logging.info('Now WiMAX. Switch to WiMAX2+')
        set_mode(br, '2')
        set_mode(br, '1')


def set_mode(br, val):
    logging.info('Set mode to %s' % val)
    br.select_form(name='main_form')
    br.form.find_control('BTN_CLICK').readonly = False
    br['BTN_CLICK'] = 'wan2'
    br['COM_MODE_SEL'] = [val]
    br.submit()


if __name__ == "__main__":
    main()
