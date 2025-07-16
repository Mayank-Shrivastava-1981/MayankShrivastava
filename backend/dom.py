from bs4 import BeautifulSoup, SoupStrainer
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
from langchain_openai import ChatOpenAI
import bs4
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma   
from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain 



from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env

openai_key = os.getenv("OPENAI_API_KEY")
print("OpenAI Key:", openai_key)












# Step 1: Set target URL and SoupStrainer
#url = "https://practicetestautomation.com/practice-test-login/"
url="https://uatidentity.landscapecrm.com/Authentication/Account/Login"
strainer = SoupStrainer("div", class_="et_pb_text_inner", id="et_pb_text_0")

# Step 2: Load and parse only needed part of DOM
loader = WebBaseLoader(url, bs_kwargs={"parse_only": strainer})
doc = loader.load()[0]
html = doc.page_content
soup = BeautifulSoup(html, "html.parser")

# Step 3: Extract all DOM elements inside the strainer
elements = []
for tag in soup.find_all(True):  # All tags
    elements.append({
        "tag": tag.name,
        "id": tag.get("id"),
        "name": tag.get("name"),
        "type": tag.get("type"),
        "class": " ".join(tag.get("class", [])),
        "text": tag.get_text(strip=True)
    })

# Step 4: Serialize DOM for the LLM
def serialize_elements(elems):
    lines = []
    for el in elems:
        lines.append(
            f"<{el['tag']} id='{el['id']}' name='{el['name']}' type='{el['type']}' class='{el['class']}' text='{el['text']}'>"
        )
    return "\n".join(lines)

serialized_dom = serialize_elements(elements)

# Step 5: Define your manual test case
test_case = """
1. Enter 'student' in the username field.
2. Enter 'Password123' in the password field.
3. Click the login button.
"""

# Step 6: Langchain Prompt to Extract ONLY Relevant Locators
template = """
You are a QA automation expert.

Based on the test case and the provided DOM, extract only the relevant element locators (e.g., tag, id, name, or a possible XPath).

DOM Elements:
{dom}

Manual Test Case:
{test_case}

Return only the matched DOM elements that are used in the test case, should be case sensitive with a short explanation and suggested locator (ID or XPath).
"""

prompt = PromptTemplate(
    input_variables=["dom", "test_case"],
    template=template
)

llm = ChatOpenAI(temperature=0, model="gpt-4")
chain = LLMChain(prompt=prompt, llm=llm)

# Step 7: Run the chain
response = chain.run({
    "dom": serialized_dom,
    "test_case": test_case
})

print("🔎 Relevant Element Locators:")
print(response)
