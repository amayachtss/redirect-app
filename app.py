from flask import Flask, redirect
import base64
import zlib

app = Flask(__name__)

@app.route("/go/<encoded>")
def go(encoded):
    try:
        padding = '=' * (-len(encoded) % 4)

        url = zlib.decompress(
            base64.urlsafe_b64decode(encoded + padding)
        ).decode()

        return redirect(url)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run()
