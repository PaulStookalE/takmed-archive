from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import BASE


# У цьому файлі створюються проміжні таблиці для зв'язків "many to many" у базі даних.


users_articles_association = Table(
    'users_articles', BASE.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('article_id', Integer, ForeignKey('articles.id'))
)

topics_articles_association = Table(
    'topics_articles', BASE.metadata,
    Column('topic_id', Integer, ForeignKey('topics.id')),
    Column('article_id', Integer, ForeignKey('articles.id'))
)

tags_articles_association = Table(
    'tags_articles', BASE.metadata,
    Column('tag_id', Integer, ForeignKey('tags.id')),
    Column('article_id', Integer, ForeignKey('articles.id'))
)