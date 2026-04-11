from typing import List
from fastapi import FastAPI, Depends, status, Response , HTTPException
from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,  models ,database, oauth2
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(
                    tags=['blog'],
                    prefix='/blog'
                    )
get_db = database.get_db

@router.get('/' , response_model = List[schemas.ShowBlog])
def all(db : Session = Depends(database.get_db), current_user = Depends(oauth2.get_current_user)):
   return blog.get_all(db)

@router.post('/',  status_code = status.HTTP_201_CREATED)
def create_db(request : schemas.Blog, db:Session = Depends(get_db),current_user = Depends(oauth2.get_current_user)):
    return blog.create(request,db)
    


@router.get('/{id}', status_code = 200 , response_model = schemas.ShowBlog)
def show(id:int,  db : Session = Depends(get_db),current_user = Depends(oauth2.get_current_user)):
    return blog.show_id(id,db)

@router.delete('/{id}',status_code = status.HTTP_204_NO_CONTENT)
def delete(id, db :Session = Depends(get_db),current_user = Depends(oauth2.get_current_user)):
    return blog.delete(id,db)

@router.put('/{id}',status_code = status.HTTP_202_ACCEPTED)
def update(id, request : schemas.Blog, db : Session = Depends(get_db),current_user = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

