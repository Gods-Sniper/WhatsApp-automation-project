from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Setup database connection (SQLite example)
engine = create_engine('sqlite:///example.db')
Base = declarative_base()

# Define tables as Python classes
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Relationships
    messages = relationship("Message", back_populates="user")
    contacts = relationship("Contact", back_populates="user")

class Status(Base):
    __tablename__ = 'statuses'
    id = Column(Integer, primary_key=True)
    status_content = Column(String, nullable=False, unique=True)  # E.g., Active, Inactive, etc.
    user_id = Column(Integer, ForeignKey('users.id'))  # Foreign key to User table

class ScheduledTask(Base):
    __tablename__ = 'scheduled_tasks'
    id = Column(Integer, primary_key=True)
    frequency = Column(DateTime)  # Fixed Column Definition

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))  # Foreign key to User table

    # Relationships
    user = relationship("User", back_populates="messages")

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    contact_name = Column(String, nullable=False)
    phone_nb = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))  # Foreign key to User table

    # Relationships
    user = relationship("User", back_populates="contacts")

# Create all tables in the database
Base.metadata.create_all(engine)
print("Tables created!")

# Example: Add data using a session
Session = sessionmaker(bind=engine)
session = Session()

# Add sample data
user1 = User(username="JohnDoe", email="johndoe@example.com")
contact1 = Contact(contact_name="Jane Doe", phone_nb="+123456789", user=user1)
message1 = Message(content="Hello, Jane!", user=user1)
status1 = Status(status_content="Active", user_id=user1.id)

# Add and commit to the database
session.add(user1)
session.add(contact1)
session.add(message1)
session.add(status1)
session.commit()
print("Sample data added!")

# List all tables in the database
import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables in database:", cursor.fetchall())
conn.close()
