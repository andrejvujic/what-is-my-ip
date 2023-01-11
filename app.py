from flask import Flask, request, jsonify

app = Flask(__name__)

HOST = "0.0.0.0"
PORT = 3333


@app.route("/", methods=["GET"])
def index():
    def formatted_response(
        _: str,
    ) -> list[str]:
        _ = _.split(
            ",",
        )

        _ = [e.strip() for e in _]

        if not len(
            _,
        ):
            return jsonify(
                {
                    "length": 1,
                    "ip": "unknown",
                },
            )

        return jsonify(
            {
                "length": len(
                    _,
                ),
                "ip": _ if len(
                    _,
                ) > 1 else _[0],
            }
        )

    if not request.environ.get(
        "HTTP_X_FORWARDED_FOR",
    ):
        print("4")
        return formatted_response(
            request.environ["REMOTE_ADDR"],
        )
    else:
        return formatted_response(
            request.environ["HTTP_X_FORWARDED_FOR"],
        ),


if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT,
    )
