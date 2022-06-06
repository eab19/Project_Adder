from app.models import User, Post, Comment, Vote
from app.db import Session, Base, engine
# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()
# insert users
db.add_all([
  User(username='test', email='test@test.com', password='password123')
])
db.commit()
# insert posts
db.add_all([
  Post(title='Donec posuere metus vitae ipsum', post_url='/', user_id=1)
])

db.commit()

# insert comments
db.add_all([
  Comment(comment_text='Nunc rhoncus dui vel sem.', user_id=1, post_id=1)
])
db.commit()

# insert votes
db.add_all([
  Vote(user_id=1, post_id=1)
])
db.commit()

db.close()