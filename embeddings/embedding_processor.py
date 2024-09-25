from sentence_transformers import SentenceTransformer
import numpy as np
import psycopg2
from database.db_manager import connect_db

# بارگذاری مدل برای تبدیل متن به embedding
model = SentenceTransformer('all-MiniLM-L6-v2')

# تابع برای تبدیل Markdown به embedding
def convert_markdown_to_embedding(markdown_content):
    embedding = model.encode(markdown_content)
    return embedding

# تابع برای ذخیره embedding در پایگاه داده
def save_embedding(filename, embedding):
    conn = connect_db()
    cur = conn.cursor()
    try:
        # تبدیل به لیست برای ذخیره
        embedding_list = embedding.tolist()
        cur.execute("INSERT INTO embeddings (filename, embedding) VALUES (%s, %s)", (filename, embedding_list))
        conn.commit()
        print(f"Saved embedding for {filename}")
    except Exception as e:
        print(f"Error saving embedding: {e}")
    finally:
        cur.close()
        conn.close()

markdown_content = "crawelMd"  # اینجا محتوای Markdown واقعی خود را قرار دهید
embedding = convert_markdown_to_embedding(markdown_content)
