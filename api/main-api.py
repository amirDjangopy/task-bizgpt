from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Body
from pydantic import BaseModel
from database.db_manager import connect_db

app = FastAPI()

# تعریف مدل برای پارامتر ورودی
class QueryRequest(BaseModel):
    query: str
    limit: int = 10

@app.post("/search/")
async def search(request: QueryRequest):
    query = request.query  # دریافت query از مدل
    conn = connect_db()
    cur = conn.cursor()
    try:
        # اینجا می‌توانید شرط جستجو را بر اساس نیاز خود اضافه کنید
        cur.execute("SELECT * FROM embeddings WHERE filename ILIKE %s;", (f'%{query}%',))
        results = cur.fetchall()
        if results:
            return JSONResponse(content={"results": results})
        else:
            return JSONResponse(content={"detail": "No embeddings found in the database."}, status_code=404)
    except Exception as e:
        return JSONResponse(content={"detail": f"Error fetching embeddings: {e}"}, status_code=500)
    finally:
        cur.close()
        conn.close()
