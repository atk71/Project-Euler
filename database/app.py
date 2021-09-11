import spacy
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from extract_keywords import extract_keywords
from get_fuzzy_similarity import get_fuzzy_similarity

import subprocess

# load the (small/large) engine language model

model_size = 'sm'  # (sm/lg)
language_model = "en_core_web_" + model_size
subprocess_call = "python -m spacy download " + language_model
subprocess.call(subprocess_call, shell=True)

app = Flask(__name__)
CORS(app)

nlp = spacy.load(language_model)
print(f"Loaded {model_size.capitalize()} language model")


@app.route('/api/keywords', methods=['POST'])
def get_keywords():
    query_string = request.json.get("query_string")
    tags = request.json.get("tags")
    keywords = extract_keywords(nlp, query_string, tags)
    return jsonify(keywords=keywords)


@app.route('/api/fuzzy-matches', methods=['POST'])
def get_fuzzy_matches():
    token = request.json.get("token")
    dictionary = request.json.get("dictionary")
    similar_words = get_fuzzy_similarity(token, dictionary)
    return jsonify(similar_words=similar_words)
