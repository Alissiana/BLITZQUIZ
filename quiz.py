from flask import Flask, render_template, request
import random, copy

app = Flask(__name__)


original_questions = { # Словарь с вопросами
    # Format is 'question':[options]
    'Taj Mahal': ['Agra', 'New Delhi', 'Mumbai', 'Chennai'],
    'Great Wall of China': ['China', 'Beijing', 'Shanghai', 'Tianjin'],
    'Petra': ['Ma\'an Governorate', 'Amman', 'Zarqa', 'Jerash'],
    'Machu Picchu': ['Cuzco Region', 'Lima', 'Piura', 'Tacna'],
    'Egypt Pyramids': ['Giza', 'Suez', 'Luxor', 'Tanta'],
    'Colosseum': ['Rome', 'Milan', 'Bari', 'Bologna'],
    'Christ the Redeemer': ['Rio de Janeiro', 'Natal', 'Olinda', 'Betim']
}

questions = copy.deepcopy(original_questions)



def shuffle(q): # Функция, которая рандомизирует значения из словаря
    """
    This function is for shuffling
    the dictionary elements.
    """
    selected_keys = []
    i = 0
    while i < len(q):
        current_selection = random.choice(list(q.keys()))
        if current_selection not in selected_keys:
            selected_keys.append(current_selection)
            i = i + 1
    return selected_keys


@app.route('/', methods=['GET'])
def quiz(): # Функция для формирования викторины, также рендерит html
    questions_shuffled = shuffle(questions)
    for i in questions.keys():
        random.shuffle(questions[i])
    return render_template('main.html', q=questions_shuffled, o=questions)


@app.route('/quiz', methods=['POST'])
def quiz_answers(): # Функция подсчёта и вывода правильных ответов
    correct = 0
    for i in questions.keys():
        answered = request.form[i]
        if original_questions[i][0] == answered:
            correct = correct + 1
    return f"""<h3 style="border-bottom:2px solid orangered;padding-bottom:5px; background-color: #876c99; text-align: center">
       Correct: {str(correct)}</h3>
    """

if __name__ == '__main__':
    app.run(debug=True)
