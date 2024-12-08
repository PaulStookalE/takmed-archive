from .base import BASE
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .relationships import users_articles_association


class User(BASE):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(40), nullable=False)
    is_admin = Column(Boolean, nullable=False)

    # Створення зв'язку (one to many) користувача зі статтями.
    user_articles = relationship('Article', backref='article')

    # Створення зв'язку (many to many) за допомогою проміжної таблиці (user_article_association) між користувачами та статтями які вони уподобали.
    favorite_articles = relationship('Article', secondary=users_articles_association, back_populates='users_that_liked')