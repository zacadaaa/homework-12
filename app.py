from flask import Flask, request, render_template, send_from_directory
from functions import get_tags_from_posts_file, get_posts_by_tag,  upload_image, save_post

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    tags = get_tags_from_posts_file(POST_PATH)
    return render_template("index.html", tags=tags)


@app.route("/tag")
def page_tag():

    tag = request.values.get("tag")

    if tag:
        posts_match = get_posts_by_tag(tag, POST_PATH)
        return render_template("post_by_tag.html", tag=tag, posts=posts_match)
    return "тэг не задан"



@app.route("/post", methods=["GET", "POST"])
def page_post_create():

    if request. method=="POST":
        picture, content = request.files.get("picture"), request.form.get("content")

        if picture and content:
            picture_url = upload_image(picture, UPLOAD_FOLDER)
            post_data = {"pic": "/"+picture_url, "content": content}
            save_post(POST_PATH, post_data)

            return render_template("post_uploaded.html", post_data=post_data)
        return "Ошибка загрузки "
    return render_template("post_form.html")


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

