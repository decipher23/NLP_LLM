from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
import sqlite3
llm=ChatOpenAI(model="gpt-4o-mini")

def data1(sentence,lang_detect,language,translated,prob):
    conn=sqlite3.connect(r"C:\Users\rawat\OneDrive\Desktop\6PM\project2\review_project.db")
    cursor=conn.cursor()
    query="insert into translation(sentence,lang_detect,translatedlang,translated,prob) values(?,?,?,?,?)"
    values=(sentence,lang_detect,language,translated,prob)
    cursor.execute(query,values)
    conn.commit()

class machine_translation(BaseModel):
    lang_detect:str=Field(description="Detect the language(full name) of sentence ")
    language:str=Field(description="Language in which the sentence is translated")
    translated:str=Field(description="translated sentence")
    prob:float=Field(le=1,gt=0)
    

llm_structure=llm.with_structured_output(machine_translation)
template=PromptTemplate(template="the sentence {prompt} and Translate the above sentence into {language} ",input_variables=["prompt","language"])
chain=template|llm_structure
def translate_text(lang,language=None):
    resp=chain.invoke({"prompt":lang,"language":language})
    data1(lang,resp.lang_detect,resp.language,resp.translated,resp.prob)
    return resp

# print(resp.language)
# print(resp.translated)
# print(resp.prob)
# print(resp.lang_detect)

# data1(lang,resp.lang_detect,resp.language,resp.translated,resp.prob)
