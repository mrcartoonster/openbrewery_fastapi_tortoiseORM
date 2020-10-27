# project/app/main.py
# This is where our FastAPI endpoint routers from sponsors and beers are
# served.


from fastapi import FastAPI


app = FastAPI()


@app.get('/ping')
def pong():
    """
    Test router for settings and quick fire up.
    """
    return {'ping': 'pong!'}
