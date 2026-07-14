from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
import sqlite3

llm=ChatOpenAI(model="gpt-4o-mini")
def data1(review,sent,prob):
    conn=sqlite3.connect("review_project.db")
    cursor=conn.cursor()
    query="INSERT INTO sentiment(Sentence,Sentiment,Probability) VALUES(?,?,?)"
    values=(review,sent,prob)
    cursor.execute(query,values)
    conn.commit()

class Review(BaseModel):
    sentiment:str=Field(description="Provide sentiment of a review as positive, negative or neutral and how much probability of sureity you have ")
    prob:float=Field(le=1,gt=0)
#=========================================================================================
llm_structure=llm.with_structured_output(Review)
template=PromptTemplate(template="{prompt}",input_variables=["prompt"])
chain=template|llm_structure   
 
# ===============================================
# main function which takes the value
def predict_sentiment(review):
    resp=chain.invoke({"prompt":review})
    data1(review,resp.sentiment,resp.prob)
    return resp
# print(resp.sentiment)
# data1()
# print(resp.sentiment)
# print(resp.prob)

# data1(review,resp.sentiment,resp.prob)
# print("done")
