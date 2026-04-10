from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,models,database
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..routers import authentication
from datetime import datetime,timedelta



# router = APIRouter(
#                     tags = ['Login'],
#                     prefix = '/login'

#                  )

# @router.post('/')
# def login(request:schemas.Login, db : Session = Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.email == request.username).first()
    
#     if not user:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
#                             detail=f'User not found with user')
    
#     if not Hash.verify(user.password, request.password):
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
#                             detail=f'Incorrect password')

#     access_Token_expires = timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_Token=authentication.create_access_token(dat={"Sub": user.email})

#     return {"access taken ":access_Token,"token_type":'bearer'}

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from .. import schemas, models, database,JWT_Token
from ..hashing import Hash


router = APIRouter(
    tags=['Login'],
    prefix='/login'
)

ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.post('/')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid credentials'
        )

    if not Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid credentials'
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = JWT_Token.create_access_token(
        data={"sub": user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

