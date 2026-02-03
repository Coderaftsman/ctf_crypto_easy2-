from flask import Flask, render_template, request

app = Flask(__name__)

FLAG = "cyber{xor_is_easy}"

# XOR-encrypted hex (single-byte key challenge)
CIPHER_HEX = "0a1b081e0b6b0c1b1f1c1d0b6b1c0a6b0d0c06"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        answer = request.form.get("answer", "")
        if answer == FLAG:
            return render_template("success.html", flag=FLAG)
        else:
            return render_template(
                "index.html",
                cipher=CIPHER_HEX,
                error=True
            )

    return render_template("index.html", cipher=CIPHER_HEX)
