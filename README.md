Story Template Project
The Story Template Project is a Python program that allows users to create completed stories by filling in placeholders in a template file. The program utilizes an SQLite database to store user information, words entered by users, and completed stories.

Features
Prompt users to enter their username and email.
Load a template file containing placeholders for words.
Prompt users to enter words corresponding to each placeholder.
Store user information in the "users" table of the database.
Store entered words and their corresponding types in the "words" table of the database.
Generate a completed story by replacing the placeholders in the template file with user-entered words.
Store the completed story, template file name, and associated word and user IDs in the "completed_stories" table of the database.

Prerequisites
Python 3.x
SQLite3

Usage
Enter the title of the story.
Enter your username.
Enter your email.
Enter the name of the template file (e.g., "template.txt").
Fill in each prompted word corresponding to the placeholders in the template file.
The completed story will be displayed on the console.
The completed story, template file name, and associated word and user IDs will be stored in the database.
Database
The program utilizes an SQLite database to store user information, words, and completed stories. The database file is named "project.db" and is created in the project directory.

The database schema consists of the following tables:

users: Stores user information, including the user's ID, username, and email.
words: Stores entered words and their corresponding types, along with the associated user ID.
completed_stories: Stores completed stories, along with the associated word and user IDs.
