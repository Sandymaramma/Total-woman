from SIMPLE_FLASK_APP import create_app

app = create_app()


@app.route("/totalwoman", methods=["GET"])
def totalwoman_check():
    return "ok"


@app.route("/users", methods=["GET"])
def get_all_users():
    all_users = [{"id": 1, "name": "mobola"}, {"id": 2, "name": "comfort"}, {"id": 3, "name": "gbeminiyi"}, {"id": 3, "name": "sandra"}]
    return jsonify(all_users)


if __name__ == "__main__":
    app.run(host="127.0.0.1")
