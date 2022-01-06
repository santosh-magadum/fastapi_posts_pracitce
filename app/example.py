# import os

# name=os.getenv("MYSQL_DB_URL")
# print(name)

from pydantic import BaseModel

class Team(BaseModel):
    name:str
    member_id:int
    qualification:str

    class Config:
        orm_mode =True


team={"name":"santu",
      "member_id":"da"}
    #   "qualification":"BE"}

def func_(t: Team):
    print(t)

# func_(team)


from typing import List
from pydantic import BaseModel


class Foo(BaseModel):
    count: int
    size: float = None


f=Foo(count='fafa')
print(f)
class Bar(BaseModel):
    apple = 'x'
    banana = 'y'


class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]


# m = Spam(foo={'count': "dpo"}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
# print(m)

def plan(foo:Foo):
    print(foo)

# plan({'count': "dpo"})

def execute(marks:int):
    print(marks)

# execute("jfklakjf")