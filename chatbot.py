import os
import PyPDF2
from langchain_openai import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Inisialisasi LLM dari OpenAI
llm = OpenAI(model="gpt-3.5-turbo-instruct")
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
    return text

def get_all_pdfs_text(upload_folder):
    all_texts = []
    for filename in os.listdir(upload_folder):
        if filename.endswith('.pdf'):
            file_path = os.path.join(upload_folder, filename)
            all_texts.append(read_pdf(file_path))
    return all_texts

def split_text(text, max_tokens=2000):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        if current_length + len(word) + 1 > max_tokens:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_length = 0
        current_chunk.append(word)
        current_length += len(word) + 1

    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

def chatbot_response(user_input, upload_folder):
    pdf_texts = get_all_pdfs_text(upload_folder)
    relevant_text = ""
    for text in pdf_texts:
        text_chunks = split_text(text)
        for chunk in text_chunks:
            if user_input.lower() in chunk.lower():
                relevant_text += chunk + "\n\n"

    prompt = f"{relevant_text}\n\nUser: {user_input}\nChatbot:"
    response = conversation.run(prompt)
    return response