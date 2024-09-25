import psycopg2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# تابع اتصال به دیتابیس PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="embedding_db",
            user="bizgpt",
            password="biz"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise

# # بازیابی تمامی بردارهای ذخیره شده در دیتابیس
# def fetch_all_embeddings():
#     conn = connect_db()
#     cur = conn.cursor()

#     try:
#         # دریافت بردارهای embedding از دیتابیس
#         cur.execute("SELECT filename, embedding FROM embeddings")
#         records = cur.fetchall()

#         # بررسی اینکه آیا بردارها وجود دارند یا خیر
#         if not records:
#             raise Exception("No embeddings found in the database.")

#         embeddings = {}
#         for record in records:
#             filename = record[0]
#             # فرض می‌کنیم embedding به صورت آرایه NumPy در پایگاه داده ذخیره شده است
#             embedding = np.frombuffer(record[1], dtype=np.float32)  # استفاده از frombuffer برای تبدیل به آرایه
#             embeddings[filename] = embedding

#     except Exception as e:
#         print(f"Error fetching embeddings: {e}")
#         raise
#     finally:
#         cur.close()
#         conn.close()

#     return embeddings

# # پیدا کردن نزدیک‌ترین بردارها بر اساس شباهت کسینوسی
# def find_similar_embeddings(query_embedding, stored_embeddings, top_n=5):
#     """
#     مقایسه بردار کاربر با بردارهای ذخیره شده و بازگرداندن نزدیک‌ترین‌ها
#     """
#     if not stored_embeddings:
#         raise Exception("No stored embeddings available for comparison.")

#     similarities = []
#     filenames = []

#     # محاسبه شباهت کسینوسی
#     for filename, embedding in stored_embeddings.items():
#         try:
#             similarity = cosine_similarity([query_embedding], [embedding])[0][0]
#             similarities.append(similarity)
#             filenames.append(filename)
#         except Exception as e:
#             print(f"Error calculating similarity for {filename}: {e}")
#             continue

#     # بررسی اینکه آیا شباهتی پیدا شده است
#     if not similarities:
#         raise Exception("No similar embeddings found.")

#     # مرتب‌سازی نتایج بر اساس شباهت و انتخاب نزدیک‌ترین‌ها
#     sorted_indices = np.argsort(similarities)[::-1]
#     top_filenames = [filenames[i] for i in sorted_indices[:top_n]]
#     top_similarities = [similarities[i] for i in sorted_indices[:top_n]]

#     # برگرداندن نتایج به صورت لیستی از نام فایل و میزان شباهت
#     results = [{"filename": top_filenames[i], "similarity": top_similarities[i]} for i in range(top_n)]
#     return results
