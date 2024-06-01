from flask import Flask, render_template, request
import os
import openai

# Replace with your OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = "sk-proj-6iSZnIijtets51wEkCNwT3BlbkFJ6wBtEnb22T3NVaGLgkC3"


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def generate_image():
    if request.method == "POST":
        user_prompt = request.form["prompt"]

        # Generate the image using OpenAI
        response = openai.Image.create(
            prompt=user_prompt,
            n=1,
            size="1024x1024",
        )
        image_url = response["data"][0]["url"]

        print(app.template_folder)

        return render_template("index.html", image_url=image_url)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
