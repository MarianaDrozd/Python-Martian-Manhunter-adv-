"""Data models."""
from app import db


class User(db.Model):
    """Data model for user accounts."""
    __tablename__ = 'users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    bio = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )
    admin = db.Column(
        db.Boolean,
        index=False,
        unique=False,
        nullable=False
    )
    articles = db.relationship("Article", backref='author', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created": str(self.created),
            "bio": self.bio,
            "admin": self.admin
        }


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(
        db.String(255),
        nullable=False,
        index=True,
        unique=False
    )
    slug = db.Column(
        db.String(50),
        nullable=False,
        index=True,
        unique=False
    )
    description = db.Column(
        db.Text,
        nullable=False,
        index=False,
        unique=False
    )
    short_description = db.Column(
        db.String(350),
        nullable=True,
        index=False,
        unique=False
    )
    img = db.Column(
        db.String(255),
        nullable=True,
        index=False,
        unique=False
    )

    @property
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "slug": self.slug,
            'description': self.description,
            "short_description": self.short_description,
            "img": self.img
        }


class Category(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(350)
    )
