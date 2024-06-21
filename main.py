from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import api


description = """
------------------------------
**Username and password for Admin**
* Login: **admin2003**
* Parol: **admin2003**
------------------------------
"""

app = FastAPI(
    description=description,
    contact={
        'name': "Xurshidbek Tursunaliyev's telegram account url for questions",
        'url': 'https://t.me/fastapi_developer1',
    },
    docs_url='/',
    redoc_url='/redoc',
)

app.include_router(api)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
