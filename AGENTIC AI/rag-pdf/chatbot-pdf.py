
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import tempfile
import os

load_dotenv()

st.title("Document Q&A Chatbot")

uploaded_file = st.file_uploader(
    "Upload PDF or TXT", type=["pdf", "txt"]
)

if uploaded_file:
    suffix = os.path.splitext(uploaded_file.name)[1].lower()

    with tempfile.NamedTemporaryFile(
        delete=False, suffix=suffix
    ) as f:
        f.write(uploaded_file.getvalue())
        path = f.name

    try:
        loader = (
            PyPDFLoader(path)
            if suffix == ".pdf"
            else TextLoader(path, encoding="utf-8")
        )

        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(docs)

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        db = Chroma.from_documents(chunks, embeddings)

        st.success("Document processed successfully!")

        question = st.text_input("Ask a question about your document")

        if st.button("Get Answer") and question.strip():
            results = db.similarity_search(question, k=2)

            context = "\n\n".join(
                d.page_content for d in results
            )

            prompt = f"""Answer using ONLY the context below.
If the answer is not present, say:
'Information not found in the uploaded document.'

Context:
{context}

Question: {question}"""

            llm = ChatGroq(
                model="openai/gpt-oss-20b",
                temperature=0
            )

            st.write(llm.invoke(prompt).content)

            st.subheader("Sources")

            for d in results:
                page = d.metadata.get("page")

                st.write(
                    f"{d.metadata.get('source', uploaded_file.name)}"
                    + (f" — Page {page + 1}" if page is not None else "")
                )

    except Exception as e:
        st.error(f"Error: {e}")

    finally:
        if os.path.exists(path):
            os.remove(path)
