from fastapi import APIRouter,Depends,status, HTTPException
from .. import schemas,models,database
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user

router = APIRouter(
                    tags = ['user'],
                    prefix = '/user'
)


get_db = database.get_db

@router.post('/', status_code = status.HTTP_201_CREATED, response_model = schemas.ShowUser)
def user_add(request : schemas.User,db : Session = Depends(get_db)):
    return user.user_add(request,db)

@router.get('/{id}', status_code = status.HTTP_302_FOUND , response_model = schemas.ShowUser)
def show(id : int ,db : Session = Depends(get_db)):
    return user.show(id,db)
