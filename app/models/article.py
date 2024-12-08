from .base import BASE
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from .relationships import users_articles_association, topics_articles_association, tags_articles_association



class Article(BASE):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=False)
    text = Column(Text, nullable=False)

    # Створення зв'язку статті з конкретним користувачем.
    article_id = Column(Integer, ForeignKey('users.id'))

    # Створення зв'язку (many to many) за допомогою проміжної таблиці (user_article_association) між статтями та користувачами які уподобали статтю.
    users_that_liked = relationship('User', secondary=users_articles_association, back_populates='favorite_articles')

    # Створення зв'зку (many to many) за допомогою проміжної таблиці (topic_article_association) між статтями та темами (топіками) до яких вони відносяться.
    topics = relationship('Topic', secondary=topics_articles_association, back_populates='articles')

    # Створення зв'зку (many to many) за допомогою проміжної таблиці (tags_articles_association) між статтями та тегами які до них відносяться.
    tags_for_articles = relationship('Tag', secondary=tags_articles_association, back_populates='articles_for_tags')

    number_of_views = 0

    # Створення зв'язку (one to many) між картинками та статтею до якої вони відносяться.
    images = relationship('Image', backref='article_to_wich_belongs')