from key import OPENai_KEY
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader

llm = ChatOpenAI(openai_api_key=OPENai_KEY)



