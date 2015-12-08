import asyncio
import logging

from aiohttp.web import WebSocketResponse
from aiohttp.wsgi import WSGIServerHttpProtocol
from gunicorn.workers.gaiohttp import AiohttpWorker


class WSGIWebsocketProtocol(WSGIServerHttpProtocol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = self.wsgi
        self.app.loop = asyncio.get_event_loop()

    def create_wsgi_environ(self, message, payload):
        environ = super().create_wsgi_environ(message, payload)
        environ['wsgi.websocket'] = None
        self.method = message.method
        self.headers = message.headers
        self._writer = self.writer
        self._reader = self.reader
        self.version = message.version
        self.path = environ.get('PATH_INFO', '')
        ws = WebSocketResponse()
        ok, protocol = ws.can_start(self)
        if ok:
            ws.start(self)
            environ['wsgi.websocket'] = ws
        return environ


class AiohttpWebsocketWorker(AiohttpWorker):
    def factory(self, wsgi, addr):
        is_debug = self.log.loglevel == logging.DEBUG

        proto = WSGIWebsocketProtocol(
            wsgi, readpayload=True,
            loop=self.loop,
            log=self.log,
            debug=is_debug,
            keep_alive=self.cfg.keepalive,
            access_log=self.log.access_log,
            access_log_format=self.cfg.access_log_format,
        )
        return self.wrap_protocol(proto)
