from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import requests
import json

BINANCE_FAPI = "https://fapi.binance.com/fapi/v1/klines"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        qs = parse_qs(urlparse(self.path).query)

        symbol = qs.get("symbol", ["BTCUSDT"])[0]
        interval = qs.get("interval", ["1m"])[0]
        limit = qs.get("limit", ["200"])[0]

        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }

        r = requests.get(BINANCE_FAPI, params=params, timeout=8)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(r.content)
