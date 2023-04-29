from fastapi import FastAPI


web_app = FastAPI()


@web_app.get('/')
def hello():
    return {'message': 'hello'}


@web_app.on_event('startup')
async def on_start():
    ...


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(web_app, host="0.0.0.0", port=8000)
