from fastapi import APIRouter, HTTPException, Request
from config.db import conn
from models.user import music
from schemas.music import Music

user = APIRouter()

@user.get('/')
def home():
    return "Hello world"

@user.get('/posts')
def get_posts():
    result = conn.execute(music.select()).fetchall()
    return [dict(r) for r in result]

@user.post('/posts')
def create_music(new_music: Music, request: Request):
    try:
        new_music_data = {
            "GeneroMusical": new_music.GeneroMusical,
            "NombreBanda": new_music.NombreBanda,
            "Exito": new_music.Exito,
        }
        result = conn.execute(music.insert().values(new_music_data))
        conn.commit()
        return {"message": "Music record created successfully", "id": result.lastrowid}
    except Exception as e:
        print(f"Error: {e}")
        print(f"Request data: {request.json()}")
        raise HTTPException(status_code=400, detail=str(e))


@user.put('/posts/{music_id}')
async def update_music(music_id: int, updated_music: Music):
    try:
        updated_music_data = {
            "GeneroMusical": updated_music.GeneroMusical,
            "NombreBanda": updated_music.NombreBanda,
            "Exito": updated_music.Exito,
        }
        stmt = (
            music.update()
            .where(music.c.id == music_id)
            .values(updated_music_data)
        )
        result = conn.execute(stmt)
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Music with id {music_id} not found")
        return {"message": f"Music with id {music_id} updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
@user.delete('/posts/{music_id}')
async def delete_music(music_id: int):
    try:
        stmt = music.delete().where(music.c.id == music_id)
        result = conn.execute(stmt)
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Music with id {music_id} not found")
        return {"message": f"Music with id {music_id} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 