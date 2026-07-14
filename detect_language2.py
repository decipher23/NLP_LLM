from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
import sqlite3 

llm=ChatOpenAI(model="gpt-4o-mini")
def data1(sentence,lang_detect,prob):
    conn=sqlite3.connect(r"C:\Users\rawat\OneDrive\Desktop\6PM\project2\review_project.db")
    cursor=conn.cursor()
    query="insert into langtable(sentence,lang_detect,prob) values(?,?,?)"
    values=(sentence,lang_detect,prob)
    cursor.execute(query,values)
    conn.commit()

class Review(BaseModel):
    language:str=Field(description="Detect the language of sentence and how much probability of sureity you have ")
    prob:float=Field(le=1,gt=0)

llm_structure=llm.with_structured_output(Review)
template=PromptTemplate(template="{prompt}",input_variables=["prompt"])
chain=template|llm_structure

def detect_language(sentence):
    resp=chain.invoke({"prompt":sentence})
    data1(sentence,resp.language,resp.prob)
    return resp

# print(resp.language)
# print(resp.prob)

# data1(sentence,resp.language,resp.prob)
# print("done")


