from flask import Flask, render_template_string, request

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My first project</title>
</head>
<body>
    <h1>This is my first time using Flask</h1>
    <h5>This is a new website</h5>

    <form method="POST">
        <h5>Age Calculator</h5>
        <label for="birthyear">Enter your birthyear:</label>
        <input type="number" name="birthyear" placeholder="Enter your birthyear" required>
        <button type="submit">Calculate Age</button>
    </form>

    {% if age is not none %}
        <h5>Calculated Age: {{ age }}</h5>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    age = None
    if request.method == "POST":
        birthyear = int(request.form.get("birthyear"))
        age = 2025 - birthyear
    return render_template_string(html_template, age=age)

if __name__ == "__main__":
    app.run(debug=True)
