from flask import Flask, request, jsonify

app = Flask(__name__)

HOST = "0.0.0.0"
PORT = 3333


@app.route("/", methods=["GET"])
def index():
    def _formatted_response(
        _: str,
    ):
        return jsonify(
            {
                "ip": _,
            }
        )

    if not request.environ.get(
        "HTTP_X_FORWARDED_FOR",
    ):
        return _formatted_response(
            request.environ["REMOTE_ADDR"],
        )
    else:
        return _formatted_response(
            request.environ["HTTP_X_FORWARDED_FOR"],
        ),


if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT,
    )
