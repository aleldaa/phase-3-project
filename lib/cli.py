#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('project.db')
cursor = conn.cursor()

title = input("Enter the title of the story: ")
username = input('Enter your username: ')
email = input('Enter your email: ')
story_template = input("Enter the name of the template file: ")

if __name__ == '__main__':
    with open(story_template, 'r') as file:
        template = file.read()

words = template.split()

for i in range(len(words)):
    if words[i].startswith('[') and words[i].endswith(']'):
        part_of_speech = words[i][1:-1]
        user_input = input(f"Enter a {part_of_speech}: ")
        words[i] = user_input
        cursor.execute("INSERT INTO words(word_type, word_text) VALUES (?, ?)",
                        (part_of_speech, user_input))

completed_story = ' '.join(words)

print(completed_story)

cursor.execute("INSERT INTO users(username, email) VALUES (?, ?)",
                (username, email))

cursor.execute("INSERT INTO completed_stories(title, story_template, completed_story) VALUES (?, ?, ?)",
                (title, story_template, completed_story))
conn.commit()