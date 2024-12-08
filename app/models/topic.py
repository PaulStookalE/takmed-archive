from .base import BASE
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .relationships import topics_articles_association


class Topic(BASE):
    __tablename__ = 'topics'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=False)

    # Створення зв'зку (many to many) за допомогою проміжної таблиці (topic_article_association) між темами (топіками) та статтями які до них відносяться.
    articles = relationship('Article', secondary=topics_articles_association, back_populates='topics')