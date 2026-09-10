from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def diary():
    if request.method == "POST":
        entry = request.form.get("entry", "").strip()

        if entry:
            with open("diary.txt", "a", encoding="utf-8") as file:
                file.write(entry + "\n")
                file.write("-" * 40 + "\n")

        return redirect("/")

    with open("index.html", "r", encoding="utf-8") as file:
        return file.read()
@app.route("/style.css")
def style():
    with open("style.css", "r", encoding="utf-8") as file:
        return file.read(), 200, {"Content-Type": "text/css"}
if __name__ == "__main__":
    app.run(debug=True)
