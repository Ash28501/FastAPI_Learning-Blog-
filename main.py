# from fastapi import FastAPI
from typing import Optional
# from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def index():
    return {'data':{'name':'Ashray'}}

@app.get('/blog')
def about(limit = 10 ,published: bool = True ,sort: Optional[str] = None):
    if published == True:
        # only get 10 published blog
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data':f"{limit} blogs from db"}

@app.get('/blog/unpublished')
def show():
    # fetch blog with id = id 
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
    # fetch blog with id = id 
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
     # fetch blog with id = id 
     return {'data': {'1','2'}}

class Blog(BaseModel):
    title : str
    body  : str
    published_at : Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    
    return {'data':f'blog is created with title as {blog.title}'}