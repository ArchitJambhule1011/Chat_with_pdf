# Question Your PDF

Question Your PDF is a Streamlit web application that allows you to ask questions about a PDF document using question-answering techniques powered by the Language Learning Model Server (LLMS).

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/ArchitJambhule1011/Chat_with_pdf.git
   cd your-repo

2. Install the required dependencies:

   ```pip install -r requirements.txt

3. Run the application:

   ```streamlit run app.py

4. Access the application in your web browser at

How It Works:

Upload your PDF file by clicking on the "Upload your pdf" button.

Once the PDF is uploaded, the application will extract the text from the PDF and split it into chunks using the CharacterTextSplitter from the langchain library.

Enter your question in the text input box labeled "Ask your question".

The application uses the OpenAI embeddings from the langchain library to create a vector base from the text chunks using the FAISS vector store.

The Language Learning Model Server (LLMS) from the langchain library is utilized to load a question-answering chain of your choice. This chain is responsible for providing answers to the user's questions based on the vectorized documents and the input question.

Click the "Submit" button or press Enter to get the answer to your question. The response is obtained by running the question-answering chain on the vectorized documents and the user's question.

Dependencies

streamlit: Used to create the web application.

PyPDF2: Used to read and extract text from PDF files.

langchain: A package for text processing and question-answering that includes LLMS for loading and using language models.

openai: for accesing the llm

Other required dependencies can be found in the requirements.txt file.

Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

License

This project is licensed under the MIT License.    
   
