def save_picture(picture) -> str:
    """Сохраняет картинку в папку uploads"""
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path

