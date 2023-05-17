from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Create the database engine
engine = create_engine('sqlite:///project.db')
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    words = relationship('Word', back_populates='user')

# Define the Word model
class Word(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)
    word_type = Column(String)
    word_text = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='words')
    completed_stories = relationship('CompletedStory', back_populates='word')

# Define the CompletedStory model
class CompletedStory(Base):
    __tablename__ = 'completed_stories'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    story_template = Column(String)
    completed_story = Column(String)
    word_id = Column(Integer, ForeignKey('words.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    word = relationship('Word', back_populates='completed_stories')
    user = relationship('User', backref='completed_stories')

# Create the database tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Prompt user input
title = input("Enter the title of the story: ")
username = input("Enter your username: ")
email = input("Enter your email: ")
story_template = input("Enter the name of the template file: ")

if __name__ == '__main__':
    with open(story_template, 'r') as file:
        template = file.read()

words = template.split()

# Create a new user
user = User(username=username, email=email)
session.add(user)
session.commit()

word_objs = []  # List to store Word objects

# Create word objects and associate them with the user
for i, word in enumerate(words):
    if word.startswith("[") and word.endswith("]"):
        part_of_speech = word[1:-1]
        user_input = input(f"Enter a {part_of_speech}: ")
        word_obj = Word(word_type=part_of_speech, word_text=user_input, user=user)
        word_objs.append(word_obj)  # Add word_obj to the list

        # Update the word in the template
        words[i] = user_input

# Commit the word objects to the session
session.add_all(word_objs)
session.commit()

# Update the completed story with the replaced words
completed_story = " ".join(words)

# Create a completed story
completed_story_obj = CompletedStory(
    title=title,
    story_template=story_template,
    completed_story=completed_story,
    word=word_objs[0],  # Assuming the first word is used in the story
    user=user
)
session.add(completed_story_obj)
session.commit()

# Print the completed story
print(completed_story_obj.completed_story)

# Close the session
session.close()