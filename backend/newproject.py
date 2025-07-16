from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.prompts import ChatPromptTemplate    
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
from langchain.memory import ConversationBufferMemory
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup
import bs4
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma   
from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain   


loader= TextLoader("C:\\Users\\shriv\\Documents\\Mtech\\MyFolder\\Scratch_SmartGenAI-V2\\myapp-V2\\loader\\loader.txt")
text_documents = loader.load()
#print(text_documents)



loader_web= WebBaseLoader(web_path="https://practicetestautomation.com/practice-test-login/",
                          bs_kwargs=dict(parse_only=bs4.SoupStrainer("div", class_="et_pb_text_inner",id="et_pb_text_0")))
text_documents_web = loader_web.load()
print(text_documents_web)
docs = loader.load()
soup = BeautifulSoup(docs[0].page_content, "html.parser")
text = soup.get_text()
print(text)

