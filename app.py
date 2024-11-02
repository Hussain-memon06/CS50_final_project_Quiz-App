from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed to use sessions

questions = [
    {'question': 'What is the capital of France?', 'options': ['Paris', 'London'], 'answer': 'Paris'},
    {'question': 'What is 2 + 2?', 'options': ['3', '4'], 'answer': '4'},
    {'question': 'What is the capital of Italy?', 'options': ['Rome', 'Venice'], 'answer': 'Rome'},
    {'question': 'What is 5 + 3?', 'options': ['7', '8'], 'answer': '8'}
]

@app.route('/')
def index():
    # Just render the homepage with the welcome message
    return render_template('index.html')


@app.route('/quiz/<int:question_number>', methods=['GET', 'POST'])
def quiz(question_number):
    if request.method == 'POST':
        answer = request.form.get('answer')

        if answer is None:
            # Handle the case where no option is selected
            return render_template('quiz.html', question_number=question_number, question=questions[question_number - 1], error="Please select an answer.")

        session[f'q{question_number}'] = answer.strip()  # Store answer in session

        # Redirect to the next question or to the results page
        if question_number < len(questions):
            return redirect(url_for('quiz', question_number=question_number + 1))
        else:
            return redirect(url_for('results'))

    # Pass the current question to the template
    current_question = questions[question_number - 1]
    return render_template('quiz.html', question_number=question_number, question=current_question)

@app.route('/results')
def results():
    # Retrieve the user's answers from the session
    answers = [session.get(f'q{i+1}') for i in range(len(questions))]
    correct_answers = [q['answer'] for q in questions]

    # Calculate the score
    score = sum(1 for i in range(len(answers)) if answers[i] == correct_answers[i])

    # Prepare the data to be passed to the template
    results_data = [
        {
            'question': questions[i]['question'],
            'user_answer': answers[i],
            'correct_answer': correct_answers[i]
        }
        for i in range(len(questions))
    ]

    return render_template(
        'results.html',
        score=score,
        total_questions=len(questions),
        results_data=results_data
    )

if __name__ == '__main__':
    app.run(debug=True)
