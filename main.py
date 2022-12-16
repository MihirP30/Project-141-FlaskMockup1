from flask import Flask, json, jsonify, request
import csv

articles = []

file = open('articles.csv', encoding='utf-8')
reader = csv.reader(file)

data = list(reader)
articles = data[1:]

likedArticles = []
dislikedArticles = []

app = Flask(__name__)

@app.route('/get-article')
def get_article():
    return jsonify({
        'data' : articles[0],
        'status' : 'Success',
    })

@app.route('/liked-article', methods=['POST'])
def liked_article():
    article = articles[0]
    articles = articles[1:]
    likedArticles.append(article)
    return jsonify({
        'status' : 'Success'
    }),201

@app.route('/dislike-article', methods=['POST'])
def disliked_article():
    article = articles[0]
    articles = articles[1:]
    dislikedArticles.append(article)
    return jsonify({
        'status' : 'Success'
    }),201

if __name__ == '__main__':
    app.run()