from os import environ
from pathlib import Path

from vvecon.zorion import App

environ.setdefault("AUTH_ADMIN_URL", "admin/auth")
environ.setdefault("AUTH_URL", "auth")

app = App(Path(__file__).resolve().parent)
asgi = app.asgi()
wsgi = app.wsgi()

if __name__ == "__main__":
    app.run()
