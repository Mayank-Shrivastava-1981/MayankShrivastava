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


from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env

openai_key = os.getenv("OPENAI_API_KEY")
print("OpenAI Key:", openai_key)



#-------START OF SCRIPT--------
@app.route('/extract-xpaths', methods=['GET'])
def extract_xpaths():
    try:
        url = request.args.get('url')
        testCase = request.args.get('testCase')
        if not url or not testCase:
            return jsonify({'error': 'URL and testCase are required'}), 400

        # Step 1: Set target URL and SoupStrainer
        #url = "https://practicetestautomation.com/practice-test-login/"
        #url="https://uatidentity.landscapecrm.com/Authentication/Account/Login"
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
        #test_case = """
        #1. Enter 'student' in the username field.
        #2. Enter 'Password123' in the password field.
        #3. Click the login button.


        # Step 6: Langchain Prompt to Extract ONLY Relevant Locators
        template = """
            You are a QA Automation Expert.

            Your task is to extract only the DOM elements that are directly relevant to the given manual test case.

            Input:
            ----------
            DOM Snippet:
            {dom}

            Test Case Description:
            {testCase}
            ----------

            Instructions:
            - Parse the DOM to identify only those elements that are used or interacted with in the test case.
            - For each matched element, return the full DOM tag (e.g., <input id="username" type="text" />).
            - Do not include explanations or comments.
            - Only output the matched DOM tags or a unique locator (ID or XPath if tag is not available).

            Output Format:
            <matched DOM elements or locators only>
            """

        # For added precision:
        template = template.strip().replace("\n\n", "\n").strip()

        prompt = PromptTemplate(
        input_variables=["dom", "testCase"],
        template=template
        )

        llm = ChatOpenAI(temperature=0, model="gpt-4")
        chain = LLMChain(prompt=prompt, llm=llm)

        # Step 7: Run the chain
        response = chain.run({
        "dom": serialized_dom,
        "testCase": testCase
        })

        print("🔎 Relevant Element Locators:")
        print(response)
        return jsonify({'xpaths': response})
    except Exception as e:
        import traceback
        print("Error in /extract-xpaths:", e)
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
