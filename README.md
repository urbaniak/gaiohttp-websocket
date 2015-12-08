# gaiohttp websocket

Asyncio gunicorn worker with websockets support.


## Installation

```
pip install gaiohttp-websocket
```

## Running
```
gunicorn -k gaiohttp_websocket.AiohttpWebsocketWorker wsgi:app
```

This will provide `wsgi.websocket` environment variable for websocket connections, it's an instance of `aiohttp.web.WebSocketResponse`.

## Example (Python 3.4)

This example can be used in any wsgi compatible application.

```python
ws = environ['wsgi.websocket']
while True:
  msg = yield from ws.receive()
  ws.send_str("received: %s" % msg.data)
```

