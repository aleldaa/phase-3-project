import sqlite3

conn = sqlite3.connect('project.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "username TEXT,"
               "email TEXT"
               ")")

cursor.execute("CREATE TABLE IF NOT EXISTS words ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "word_type TEXT,"
               "word_text TEXT,"
               "user_id INTEGER,"
               "FOREIGN KEY (user_id) REFERENCES users(id)"
               ")")

cursor.execute("CREATE TABLE IF NOT EXISTS completed_stories ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "title TEXT,"
               "story_template TEXT,"
               "completed_story TEXT,"
               "word_id INTEGER,"
               "user_id INTEGER,"
               "FOREIGN KEY (word_id) REFERENCES words(id),"
               "FOREIGN KEY (user_id) REFERENCES users(id)"
               ")")

title = input("Enter the title of the story: ")
username = input('Enter your username: ')
email = input('Enter your email: ')
story_template = input("Enter the name of the template file: ")

if __name__ == '__main__':
    with open(story_template, 'r') as file:
        template = file.read()

words = template.split()

cursor.execute("INSERT INTO users(username, email) VALUES (?, ?)",
               (username, email))
user_id = cursor.lastrowid

for i in range(len(words)):
    if words[i].startswith('[') and words[i].endswith(']'):
        part_of_speech = words[i][1:-1]
        user_input = input(f"Enter a {part_of_speech}: ")
        words[i] = user_input
        cursor.execute("INSERT INTO words(word_type, word_text, user_id) VALUES (?, ?, ?)",
                       (part_of_speech, user_input, user_id))
        word_id = cursor.lastrowid
        cursor.execute("UPDATE words SET user_id = ? WHERE id = ?", (user_id, word_id))

completed_story = ' '.join(words)

print(completed_story)

cursor.execute("INSERT INTO completed_stories(title, story_template, completed_story, word_id, user_id) VALUES (?, ?, ?, ?, ?)",
               (title, story_template, completed_story, word_id, user_id))

conn.commit()