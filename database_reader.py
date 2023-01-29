import sqlite3

conn = sqlite3.connect('score_board.db')
cursor = conn.cursor()
conn.commit()

cursor.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 10")
scores = cursor.fetchall()

for score in scores:
    print(score + "\n")

# ss = str(scores)
# print(ss)