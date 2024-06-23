from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:@localhost:3306/music")

meta = MetaData()

conn = engine.connect()