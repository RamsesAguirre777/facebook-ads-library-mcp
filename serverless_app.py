# serverless_app.py
import os
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount
from mcp.server.fastmcp import FastMCP

from facebook_ads_mcp_complete import mcp  # must exist in your code

app = Starlette(routes=[Mount("/", app=mcp.streamable_http_app())])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["*"],
    expose_headers=["Mcp-Session-Id"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
