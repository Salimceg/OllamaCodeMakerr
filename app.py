from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form.get("prompt")

    system_prompt = """
    - Always define dynamic parts (like inputs, values, or settings) as function parameters or variables.
    - Avoid hardcoding values unless absolutely necessary.
    - The output must include:
    - A short and meaningful title marked as [Title].
    - The Python code inside triple backticks (```python ... ```).
    """

    final_prompt = f"""{system_prompt}
    User request: {prompt}
    """

    payload = {
        "model": "mistral",
        "prompt": final_prompt
    }

    response = requests.post("http://localhost:11434/api/generate", json=payload, stream=True)

    collected = ""
    for line in response.iter_lines():
        if line:
            data = line.decode("utf-8")
            if '"response":"' in data:
                part = data.split('"response":"')[1].split('"')[0]
                collected += part

    title = "Answer of Ollama"
    code = collected  

    code = code.replace('\n', '<br>')
    code = code.replace('```python', '<div class="actual-code">')
    code = code.replace('```', '</div>')
    return render_template("index.html", title=title, code=code)
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5055, debug=True)
