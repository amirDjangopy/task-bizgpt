readme_content = """# پروژه کراولر و جستجوی هوشمند

این پروژه شامل سه بخش اصلی است:

1. **کراولینگ صفحات وب**: کد پایتونی که 5 صفحه دلخواه از سایت [qavanin.ir](https://qavanin.ir) را کراول کرده و محتوای آن را به فرمت Markdown ذخیره می‌کند.

2. **تبدیل به Embedding**: محتوای Markdown را با استفاده از ابزارهای open source موجود به صورت vector embedding تبدیل کرده و در دیتابیس PostgreSQL ذخیره می‌کند. در صورت تمایل، می‌توانید از سایر دیتابیس‌های موجود مثل Pinecone یا Chroma نیز استفاده کنید.

3. **API جستجوی هوشمند**: با استفاده از فریمورک FastAPI، یک API طراحی شده است که درخواست کاربر را دریافت کرده و با vector embedding مقایسه می‌کند و پاسخ‌های پیشنهادی را برمی‌گرداند.

## ساختار پروژه

پروژه به صورت زیر سازمان‌دهی شده است:    

```bash
.
├── api
│   ├── __init__.py
│   ├── main-api.py
│   └── __pycache__
│       ├── __init__.cpython-311.pyc
│       ├── main-api.cpython-311.pyc
│       └── main.cpython-311.pyc
├── crawelMd
│   ├── page_1 .md
│   ├── page_2 .md
│   ├── page_3 .md
│   ├── page_4 .md
│   └── page_5 .md
├── crawler
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   └── web_crawler.cpython-311.pyc
│   └── web_crawler.py
├── database
│   ├── db_manager.py
│   ├── __init__.py
│   └── __pycache__
│       ├── db_manager.cpython-311.pyc
│       └── __init__.cpython-311.pyc
├── embeddings
│   ├── embedding_processor.py
│   ├── __init__.py
│   └── __pycache__
│       ├── embedding_processor.cpython-311.pyc
│       └── __init__.cpython-311.pyc
├── requirements.txt
├── setup.py
└── test.py
```


## نحوه راه‌اندازی پروژه

1. ** اجرای env **:

```bash
    python -m venv env

    source env/bin/activate  فعال سازی
```

2. **نصب وابستگی‌ها**:

```bash
    pip install -r requirements.txt 
```

3. **اجرای کراولر**:
برای کراول کردن صفحات وب، اسکریپت `web_crawler.py` را اجرا کنید:


4. **تبدیل Markdown به Embedding**:
بعد از کراول کردن، محتوای Markdown را به vector embedding تبدیل کرده و در دیتابیس ذخیره کنید. این کار در `embedding_processor.py` انجام می‌شود.

5. **اجرای API**:
برای راه‌اندازی API، فایل `main-api.py` را اجرا کنید:


6. **استفاده از API**:
با استفاده از CURL یا ابزارهای مشابه، می‌توانید به API متصل شوید و جستجو کنید:

```bash
curl -X POST "http://127.0.0.1:8000/search/" -H "Content-Type: application/json" -d '{"query": "a"}'
```