# 📄 DocuMind — RAG-Based PDF Question Answering Chatbot

DocuMind is a **Retrieval-Augmented Generation (RAG) chatbot** that allows users to upload a PDF document and ask questions about its content.

The application extracts text from the uploaded PDF, splits it into meaningful chunks, generates vector embeddings using **Google Gemini**, stores them in a **FAISS vector database**, retrieves the most relevant information, and uses **Gemini** to generate context-grounded answers.

---

## ✨ Features

- 📤 Upload PDF documents directly through the web interface
- 📖 Extract text from PDF files
- ✂️ Split documents into smaller chunks for efficient retrieval
- 🧠 Generate embeddings using Google Gemini
- 🔎 Perform semantic similarity search using FAISS
- 🎯 Use MMR-based retrieval to retrieve relevant and diverse document chunks
- 💬 Ask questions about the uploaded document
- 🤖 Generate answers using Google Gemini
- 🛡️ Answers are generated using the retrieved document context
- ⚡ Simple and interactive Streamlit interface

---

## 🧠 How It Works

DocuMind follows a Retrieval-Augmented Generation pipeline:

```text
        PDF Document
             │
             ▼
      Text Extraction
             │
             ▼
       Text Chunking
             │
             ▼
    Gemini Embeddings
             │
             ▼
       FAISS Vector DB
             │
             ▼
       User Question
             │
             ▼
      Similarity Search
             │
             ▼
    Relevant Context
             │
             ▼
       Gemini LLM
             │
             ▼
       Generated Answer
```

### RAG Pipeline

1. **Upload PDF**
   The user uploads a PDF document through the Streamlit interface.

2. **Text Extraction**
   Text is extracted from the PDF using `pdfplumber`.

3. **Text Chunking**
   The extracted text is divided into smaller chunks using LangChain's `RecursiveCharacterTextSplitter`.

4. **Embedding Generation**
   Google Gemini embeddings are generated for each text chunk.

5. **Vector Storage**
   The embeddings are stored in a FAISS vector database.

6. **Question Retrieval**
   When the user asks a question, relevant document chunks are retrieved using an MMR-based retriever.

7. **Answer Generation**
   The retrieved context is passed to Gemini, which generates the final answer.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| LangChain | RAG pipeline and LLM orchestration |
| Google Gemini | Embeddings and answer generation |
| FAISS | Vector database and similarity search |
| pdfplumber | PDF text extraction |
| Pydantic | API key handling |

---

## 📁 Project Structure

```text
DocuMind/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml   # Local only — DO NOT upload
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/DocuMind.git
```

### 2. Navigate to the project directory

```bash
cd DocuMind
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Configuration

DocuMind requires a **Google Gemini API key**.

Create the following file locally:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

Alternatively, you can configure the API key as an environment variable:

```text
GEMINI_API_KEY=your_api_key_here
```

### ⚠️ Security

**Never upload your API key to GitHub.**

The `.gitignore` file is configured to exclude:

```text
.streamlit/secrets.toml
.env
.venv/
venv/
__pycache__/
```

---

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

Then:

1. Upload a PDF.
2. Wait for the document to be processed.
3. Enter your question.
4. Receive an answer based on the document.

---

## 💡 Example Use Cases

DocuMind can be useful for:

- 📚 Studying academic PDFs
- 📑 Understanding technical documentation
- 📖 Question answering from books and notes
- 📝 Research document exploration
- 📋 Quickly finding information inside long PDFs
- 🎓 Educational document assistants

---

## 🚀 Future Improvements

Potential improvements include:

- Support for multiple PDF uploads
- Chat history and conversational memory
- Source/page citations in answers
- Improved document processing for scanned PDFs
- Support for additional document formats
- Persistent vector databases
- Improved UI/UX
- Streaming responses
- Document management and deletion
- Authentication and user accounts

---

## 📌 Project Highlights

- Built a complete **Retrieval-Augmented Generation (RAG)** pipeline.
- Integrated **Google Gemini** for embeddings and generative responses.
- Used **FAISS** for efficient vector similarity search.
- Implemented **MMR retrieval** for relevant and diverse context.
- Built an interactive application using **Streamlit**.
- Implemented API-key handling through environment variables and Streamlit secrets.

---

## 👨‍💻 Author

**Prashant Nain**

B.Tech — Computer Science & Engineering

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.