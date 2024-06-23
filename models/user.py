from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta,engine
music = Table("music", meta, Column("id", Integer, primary_key=True), Column(
    "GeneroMusical", String(255)), Column("NombreBanda", String(255)), Column("Exito", String(255)))

meta.create_all(engine)