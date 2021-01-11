class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mdb_user:password@127.0.0.1:60110/moviedom'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APPLICATION_PORT = 5647