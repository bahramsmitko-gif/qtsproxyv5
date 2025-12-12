from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import requests
import json

BINANCE_DEPTH = "https://fapi.binance.com/fapi/v1/depth"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        qs = parse_qs(urlparse(self.path).query)

        symbol = qs.get("symbol", ["BTCUSDT"])[0]
        limit = qs.get("limit", ["50"])[0]

        params = {
            "symbol": symbol,
            "limit": limit
        }

        r = requests.get(BINANCE_DEPTH, params=params, timeout=8)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(r.content)
