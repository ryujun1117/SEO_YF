from flask import request, redirect, url_for, render_template, flash, session, send_from_directory, send_file
from flask_blog import app
from datetime import datetime
import os
from flask_blog.add import get_info

@app.route("/", methods=["GET"])
def show_entry():
    entry = {
        "id": 1,
        "title": "Google検索結果を取得します",
        "text": "↓下に検索文字を入れて実行",
        "created_at": datetime.now()
    }
    c_path = os.getcwd()
    filepath = c_path + "/flask_blog/add/DL_BOX/result.xlsx"
    try:
        os.remove(filepath)
    except:
        pass

    return render_template("entries/show.html", entry = entry)


@app.route("/entries/show", methods=["POST"])
def get_infomation():
    word_1 = request.form.get("word_1")
    word_2 = request.form.get("word_2")
    word_3 = request.form.get("word_3")
    # word_4 = request.form.get("word_4")
    # word_5 = request.form.get("word_5")
    search_words = [word_1, word_2, word_3]
    entry = get_info.G_search(search_words)
    return render_template("entries/pandas.html",entry = entry)

@app.route("/entries/show")
def download_api():
    path = os.path.abspath(__file__)[:-14]
    return send_file(
        directory = path + '/flask_blog/add/DL_BOX',
        filename = "result.xlsx",
        as_attachment=True, 
        attachment_filename= "result.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

