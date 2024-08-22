import sqlite3

connection = sqlite3.connect('database.db')

test_post = {
    'title': 'First post',
    'post_txt': 'this is a test',
    'user_id': 0
}
with connection:
       cur = connection.cursor()
       cur.execute(
        '''
           INSERT INTO posts (post_title, post_text, user_id) 
           VALUES
            (:post_title, :post_txt, :user_id)
         ''',  
          test_post  
       )