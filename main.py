from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def home():
    advice = "This is a test advice."
    return render_template('index.html', advice=advice)
##def home():
    advice = None
    if request.method == 'POST':
        situation = request.form.get('situation')
        if situation:
            prompt_text = (
                f"You are a helpful assistant. Give a polite, clear way to say NO to avoid this situation:\n\n"
                f"Situation: {situation}\n"
                "Response:"
            )
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt_text,
                    temperature=0.7,
                    max_tokens=150,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                advice = response.choices[0].text.strip()
            except Exception as e:
                advice = f"Error: {str(e)}"
    return render_template('index.html', advice=advice)

if __name__ == '__main__':
    app.run(debug=True)