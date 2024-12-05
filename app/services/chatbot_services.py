from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from langchain.chains import ConversationalRetrievalChain
from pinecone import Pinecone
import os
from fastapi import UploadFile
from app.core.config import Settings
from app.models.response import format_response
from app.utlis.model import get_embeddings, get_llm, get_llm_gemini

settings = Settings()
INDEX_NAME = settings.INDEX_NAME
conversation_chain = None

async def process_document(file: UploadFile):
    global conversation_chain
    try:
        pc = Pinecone(
            api_key=settings.PINECONE_API_KEY
        )
        
        file_path = f"temp_{file.filename}"
        
        # Save file temporarily
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Process document
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        splits = text_splitter.split_documents(documents)
        
        # Store in Pinecone using LangChain's Pinecone vectorstore
        vector_store = LangchainPinecone.from_documents(
            documents=splits,
            embedding=get_embeddings(),
            index_name=INDEX_NAME
        )

        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=get_llm_gemini(),
            retriever=vector_store.as_retriever(),
            return_source_documents=True
        )
        
        
        # Cleanup
        os.remove(file_path)
        
        return format_response(
            code=200, 
            message="Document processed successfully and stored in Pinecone"
        )
        
    except Exception as e:
        print(str(e))
        return format_response(code=500, message=str(e))
    



async def get_chat_response(question: str):
    try:
        
        response = conversation_chain.invoke({"question": question,"chat_history":[]})
        
        return format_response(
            code=200,
            data={
                "answer": response["answer"],
                # "source_documents": [
                #     {
                #         "page_content": doc.page_content,
                #         "metadata": doc.metadata
                #     }
                #     for doc in response["source_documents"]
                # ]
            }
        )
    except Exception as e:
        print(str(e))
        return format_response(code=500, message=str(e))