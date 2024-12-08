from .base import BASE
from sqlalchemy import Column, ForeignKey, Integer, String



class Image(BASE):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    file_path = Column(String, nullable=False)

    # Створення зв'язку (one to many) між статтею та картинками які до неї відносяться.
    article_id = Column(Integer, ForeignKey('articles.id'), nullable=False)