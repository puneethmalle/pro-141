from flask import Flask, jsonify
import pandas as pd

article_data = pd.read_csv("articles.csv")

app = Flask(__name__)

articles = article_data[["title","contentType","eventType","total_events"]]
liked_articles = []
disliked_articles = []

def assign_val():
    data = {
        "title": articles.iloc[0,0],
        "contentType":articles.iloc[0,1],
        "eventType":articles.iloc[0,2],
        "total_events":articles.iloc[0,3]
    }
    return data
@app.route("/articles")
def article():
    article_data = assign_val()
    return jsonify({
        "data": article_data,
        "status": "success"

    })


@app.route("/like") 
def liked(): 
  global articles
  article_data = assign_val() 
  liked_articles.append(article_data) 
  articles.drop([0], inplace=True) 
  articles = articles.reset_index(drop=True) 
  return jsonify({ 
     "status": "success" 
    })


@app.route("/dislike")
def dislike():
    global articles
    article_data = assign_val() 
    disliked_articles.append(article_data) 
    articles.drop([0], inplace=True) 
    articles = articles.reset_index(drop=True) 
    return jsonify({ 
         "status": "success" 
    })

app.run(debug = True)