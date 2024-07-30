import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, CHAR, Date, Text, LargeBinary

from sql_app.database import Base, engine


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True, nullable=True)
    email = Column(String, unique=True, nullable=False)
    fullname = Column(String, nullable=True)
    password = Column(String(20), nullable=False)
    birthday = Column(Date, nullable=True)
    phone = Column(CHAR(13), nullable=True)
    about_me = Column(Text, nullable=True)

    def __repr__(self):
        return self.username


class Follow(Base):
    __tablename__ = "follows"
    id = Column(Integer, primary_key=True)
    follower = Column(Integer, ForeignKey("users.id"))
    following = Column(Integer, ForeignKey("users.id"))
    is_following = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


Base.metadata.create_all(engine)


