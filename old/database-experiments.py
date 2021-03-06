import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
# from sqlalchemy import Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. getting a session, which will be shared for the whole application
# 2.

print(sqlalchemy.__version__)

db_engine = create_engine("sqlite:///sqlalchemy_test.db", echo=True)


base_class = declarative_base()
base_class.metadata.create_all(db_engine)

SessionClass = sessionmaker()
SessionClass.configure(bind=db_engine)
session = SessionClass()


class KindPhrase(base_class):
    __tablename__ = "kind_phrases"

    id = Column(Integer, primary_key=True)
    phrase = Column(String)
    # starred = Column(String, default="No")

    def __repr__(self):
        return "<KindPhrase(phrase='{0}')>".format(self.phrase)
        # return "<KindPhrase(phrase='{0}', starred='{1}')>".format(self.phrase, self.starred)


# print(KindPhrase())


example_phrase = KindPhrase(phrase="new lines again")
print(example_phrase.phrase)

session.add(example_phrase)
session.commit()

count = 0
for instance in session.query(KindPhrase):
    if count == 1:
        instance.phrase += "edited"
    count += 1

session.commit()

for instance in session.query(KindPhrase):
    print(instance.phrase)

