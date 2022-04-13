"""
Модуль 2. Домашнее задание №11
Приложение на Flask.
"""

# Импорт Flask и функций.
from flask import Flask, render_template
import utils

app = Flask(__name__)

candidates_data = utils.load_candidates_from_json('candidates.json')


@app.route('/')
def index():
    return render_template('index.html', candidates=candidates_data)


@app.route('/candidate/<int:uid>')
def profile(uid):
    candidate = utils.get_candidate(uid)
    return render_template('profile.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, candidates_number=len(candidates))


@app.route('/skills/<skill>')
def get_skills(skill):
    candidates = utils.get_candidates_by_skill(skill)
    return render_template('skills.html', candidates=candidates, candidates_number=len(candidates), skill=skill)


# Запуск веб-приложения.
if __name__ == '__main__':
    app.run(debug=False)
