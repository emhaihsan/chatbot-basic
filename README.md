# Chatbot with PDF Interaction

This project is a simple chatbot application that allows users to interact with the chatbot and upload PDF files as references. The chatbot supports rendering responses in Markdown and LaTeX, making it suitable for displaying formatted text and mathematical equations.

## Features

- **Chat Interface**: Users can interact with the chatbot through a simple chat interface.
- **PDF Upload**: Users can upload PDF files to be used as references by the chatbot.
- **Markdown and LaTeX Support**: The chatbot can render responses with Markdown and LaTeX, allowing for formatted text and equations.
- **Session Management**: Users can create, rename, and delete chat sessions.

## Project Structure

```
.
├── app.py                  
├── chatbot.py              
├── templates/
│   └── index.html
│   └── upload.html
├── uploads/                
└── history/               
```

## Usage

1. **Start a New Chat**:
    - Click the "New Chat" button to start a new chat session.
    - Enter a title for the new session if desired.

2. **Send a Message**:
    - Type your message in the input field and press "Send".
    - The chatbot will respond, and the conversation will be displayed in the chat box.

3. **Edit Session Title**:
    - Click on "(Edit Title)" next to the session title to rename the current chat session.

4. **Upload a PDF**:
    - Click on "Upload PDF" to upload a PDF file to be used as a reference by the chatbot.

5. **Manage Sessions**:
    - Active sessions are listed on the left. Click on a session to switch to it.
    - Click "Delete" to remove a session.

## Dependencies

- **Flask**
- **Tailwind CSS**

## AI Tools Used

- **OpenAI API**: For generating chatbot responses.
- **LangChain**: For managing conversation history and interactions.
- **PyMuPDF (fitz)**: For extracting text from PDF documents.
- **Natural Language Toolkit (nltk)**: For processing and analyzing natural language data.


Pastikan untuk mengganti placeholder seperti `https://github.com/yourusername/chatbot-pdf-interaction.git` dengan URL repository GitHub Anda yang sebenarnya. Anda juga bisa menambahkan lebih banyak detail sesuai kebutuhan proyek Anda.
