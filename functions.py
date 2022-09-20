import json


def load_posts() -> list[dict]:
    """Чтение файла json"""
    with open('posts.json', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_word(word) -> list[dict] :
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def add_post(post: dict) -> dict:
    posts: list[dict] = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post


