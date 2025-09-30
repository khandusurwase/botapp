from configllm import llm
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')
import logging
import datetime
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory


# Logging Configuration

def setup_logger():
    log_filename = "support_bot_log.txt"
    
    logging.basicConfig(
        filename=log_filename,               # log file name
        level=logging.INFO,                  # log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="[%(asctime)s] %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s", "%H:%M:%S")
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)

def  SupportBotAgent():
    try:
        logging.info("Chat Bot Started")
        filename = 'faq.txt'
        logging.info(f"File document Fetching: {filename}")


        loader = TextLoader(filename)
        documents = loader.load()
        logging.info("Text document loading Successfull")

        logging.info("Document Splitting Startec")
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)
        print(len(texts)) 
        logging.info("Document Splitting into chunks completed")

        logging.info("Document emmbedding with OpenAIEmbeddings begin")
        ############# Text Embedding model ##################
        embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
         # store the embedding in docsearch using Chromadb
        docsearch = Chroma.from_documents(texts, embeddings) 
        print('document ingested')
        logging.info("Embedding completed")
        logging.info("chat bot Started")
        def qa():
            memory = ConversationBufferMemory(memory_key = "chat_history", return_message = True)
            qa = ConversationalRetrievalChain.from_llm(llm=llm, 
                                                    chain_type="stuff", 
                                                    retriever=docsearch.as_retriever(), 
                                                    memory = memory, 
                                                    get_chat_history=lambda h : h, 
                                                    return_source_documents=False)
            history = []
            while True:
                query = input("Question: ")
                logging.info("query in chat bot initialized")
                
                if query.lower() in ["quit","exit","bye", "by"]:
                    print("Answer: Goodbye!")
                    logging.info("quiting the app")
                    break
                    
                result = qa({"question": query}, {"chat_history": history})
                logging.info("query result fetched")

                history.append((query, result["answer"]))
                
                print("Answer: ", result["answer"])
                logging.info("query result printed successfully")

        qa()
    

    except:
         logging.error(f"Error Ocurred, something went wrong")
    
    finally:
        logging.info("Execution completed")


if __name__ == "__main__":
    setup_logger()
    SupportBotAgent()
