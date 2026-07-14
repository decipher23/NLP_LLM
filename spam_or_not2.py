from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
import sqlite3 

llm=ChatOpenAI(model="gpt-4o-mini")
def data1(email,result,prob):
    conn=sqlite3.connect(r"C:\Users\rawat\OneDrive\Desktop\6PM\project2\review_project.db")
    cursor=conn.cursor()
    query="insert into Email(email,result,prob) values(?,?,?)"
    values=(email,result,prob)
    cursor.execute(query,values)
    conn.commit()

class Review(BaseModel):
    spam:str=Field(description="Provide the result in one word that is 'spam' or 'not spam' and how much probability of sureity you have ")
    prob:float=Field(le=1,gt=0)
    

llm_structure=llm.with_structured_output(Review)
template=PromptTemplate(template="{prompt}",input_variables=["prompt"])
chain=template|llm_structure
def predict_spam(email):
    resp=chain.invoke({"prompt":email})
    data1(email,resp.spam,resp.prob)
    return resp

# print(resp.email)
# print(resp.prob)

# data1(email,resp.email,resp.prob)
# print("done")

