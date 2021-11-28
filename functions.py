import json


def get_data_from_json(path: str) -> list:
    """ Читает данные из жсон по заданному адресу"""

    f = open(path, "r")
    data = json.load(f)
    f.close()
    return data


def save_post(path: str, post_data: dict) -> bool:
    """ Сохраняет данные в жсон файл"""
    data = get_data_from_json(path)
    data.append(post_data)

    fp = open(path, "w")
    json.dump(data, fp)
    return True



def get_tags_from_posts_file(path: str) -> list:
    """ Получает из полного списка постов список тегов"""
    posts = get_data_from_json(path)
    posts_content = " ".join([p.get("content") for p in posts])
    tags = get_tags_from_str(posts_content)
    return tags


def get_tags_from_str(text: str) -> list:
    """ Вытаскивает теги из текста, возвращает списком"""

    words = text.split(" ")
    tags = [x.replace("#", "") for x in words if len(x) > 0 and x[0] == "#"]
    return tags


def get_posts_by_tag(tag: str, path:str) -> list:
    """ Вытаскивает посты по тегу из файла """

    hashtag = f"#{tag}"
    posts = get_data_from_json(path)
    posts_match = [p for p in posts if hashtag in p.get("content")]
    return posts_match


def upload_image(picture, upload_folder) -> str:
    """ Загружает картинку в папку """

    filename = f"{upload_folder}/{picture.filename}"
    picture.save(filename)
    return filename
