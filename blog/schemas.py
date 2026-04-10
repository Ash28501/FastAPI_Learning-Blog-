from pydantic import BaseModel
from typing import List,Optional

# In show only inherit tht parent class if any logic is there or else you always import the base model and see for the config according to the version.




class BlogBase(BaseModel):
    title : str
    body : str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name : str
    email : str
    password : str

class ShowUser(BaseModel):
    name : str
    email : str

    blogs : List[Blog]
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title : str
    body : str


    creator : ShowUser
    class Config():
        orm_mode= True

class Login(BaseModel):
    username : str
    password : str
    
class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    username : Optional[str] = None



