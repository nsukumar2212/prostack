
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
import os

load_dotenv()

file_path = input("Enter PDF/TXT file path: ")
suffix = os.path.splitext(file_path)[1].lower()

try:
    loader = PyPDFLoader(file_path) if suffix == ".pdf" else TextLoader(file_path, encoding="utf-8")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(chunks, embeddings)

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0
    )

    print("\nDocument processed successfully!")
    print("Ask questions about your document. Type 'exit' to stop.")

    while True:
        question = input("\nYou: ")

        if question.lower() == "exit":
            print("Chatbot closed.")
            break

        if not question.strip():
            continue

        results = db.similarity_search(question, k=4)
        context = "\n".join(doc.page_content for doc in results)

        prompt = f"""Answer ONLY using this context.
If the answer is missing, say:
Information not found in the uploaded document.

Context:
{context}

Question: {question}"""

        response = llm.invoke(prompt)

        print("\nChatbot:", response.content)

        print("\nSources:")
        for doc in results:
            print("Page:", doc.metadata.get("page", "N/A"))

except Exception as e:
    print("Error:", e)
