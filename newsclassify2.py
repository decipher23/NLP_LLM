from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
import sqlite3 

llm=ChatOpenAI(model="gpt-4o-mini")
def data1(News,Newsclassified,prob):
    conn=sqlite3.connect("review_project.db")
    cursor=conn.cursor()
    query="insert into newstable(News,Newsclassified,prob) values(?,?,?)"
    values=(News,Newsclassified,prob)
    cursor.execute(query,values)
    conn.commit()

class Review(BaseModel):
    news:str=Field(description="Detect the News category asked in prompt in one word and how much probability of sureity you have ")
    prob:float=Field(le=1,gt=0)
    

llm_structure=llm.with_structured_output(Review)
template=PromptTemplate(template="{prompt}",input_variables=["prompt"])
chain=template|llm_structure

def classify_news(news):
    resp=chain.invoke({"prompt":news})
    data1(news,resp.news,resp.prob)
    return resp
    

# print(resp.news)
# print(resp.prob)

# data1(news,resp.news,resp.prob)
# print("done")



