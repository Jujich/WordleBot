from sqlalchemy import create_engine

engine = create_engine("sqlite:///db/wordle.db", echo=True)
