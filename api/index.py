# api/index.py
from fastapi_hello.app import app
from mangum import Mangum

handler = Mangum(app)

