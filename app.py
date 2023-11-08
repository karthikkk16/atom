from flask import Flask, render_template, request, redirect, url_for, send_file
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from gtts import gTTS

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("potsawee/t5-large-generation-race-QuestionAnswer")
model = AutoModelForSeq2SeqLM.from_pretrained("potsawee/t5-large-generation-race-QuestionAnswer")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_questions", methods=["POST"])
def generate_questions():
    context = request.form["context"]
    question_type = request.form["question_type"]

    if question_type == "boolean":
        # Generate boolean questions
        inputs = tokenizer(context, return_tensors="pt")
        outputs = model.generate(inputs["input_ids"], max_length=1000, num_return_sequences=5, num_beams=5, no_repeat_ngram_size=2)
        questions = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

        boolean_questions = [f"Is it true that {question}?" for question in questions]
        return render_template("question_generation.html", questions=boolean_questions)

    elif question_type == "mcq":
        # Generate multiple-choice questions
        # Add your code to generate MCQ questions here
        pass

    elif question_type == "fill_in_the_blank":
        # Generate fill-in-the-blank questions
        # Add your code to generate fill-in-the-blank questions here
        pass

    else:
        # Handle other question types
        pass

@app.route("/generate_audio/<int:question_index>")
def generate_audio(question_index):
    text = request.args.get("text")
    tts = gTTS(text=text, lang="en")
    audio_file_path = f"question_{question_index}.mp3"
    tts.save(audio_file_path)
    return send_file(audio_file_path)

if __name__ == "__main__":
    app.run(debug=True)
