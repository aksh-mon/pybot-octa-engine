# app.py
from flask import Flask, request, render_template_string
import openai

# 1. Set your API key
openai.api_key = "YOUR_OPENAI_API_KEY"

app = Flask(__name__)

# 2. HTML form template
html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>OpenAI Prompt Demo</title>
</head>
<body>
    <h2>Enter your prompt:</h2>
    <form method="POST">
        <textarea name="prompt" rows="6" cols="60">{{prompt}}</textarea><br><br>
        <input type="submit" value="Send to OpenAI">
    </form>
    {% if response %}
    <h3>Response:</h3>
    <div style="border:1px solid #ccc; padding:10px; max-width:600px;">
        {{response|safe}}
    </div>
    {% endif %}
</body>
</html>
"""

# 3. Routes
@app.route("/", methods=["GET", "POST"])
def index():
    prompt = ""
    response = None
    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        if prompt.strip():
            result = openai.ChatCompletion.create(
                model="gpt-4o-mini",  # or "gpt-4o", "gpt-3.5-turbo"
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            response = result.choices[0].message["content"]

    return render_template_string(html_form, prompt=prompt, response=response)

if __name__ == "__main__":
    app.run(debug=True)
