from .base import BASE
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .relationships import tags_articles_association


class Tag(BASE):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    # Створення зв'зку (many to many) за допомогою проміжної таблиці (tags_articles_association) між тегами та статтями до яких вони відносяться.
    articles_for_tags = relationship('Article', secondary=tags_articles_association, back_populates='tags_for_articles')