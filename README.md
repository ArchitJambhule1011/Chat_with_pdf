# Question Your PDF

Question Your PDF is a Streamlit web application that allows you to ask questions about a PDF document using question-answering techniques powered by the Language Learning Model Server (LLMS).

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/ArchitJambhule1011/Chat_with_pdf.git
   cd your-repo

2. Install the required dependencies:

   ```pip install -r requirements.txt```

3. Run the application:

   ```streamlit run app.py```

4. Access the application in your web browser at

## How It Works:

1. Upload your PDF file by clicking on the "Upload your pdf" button.

2. Once the PDF is uploaded, the application will extract the text from the PDF and split it into chunks using the CharacterTextSplitter from the langchain library.

3. Enter your question in the text input box labeled "Ask your question".

4. The application uses the OpenAI embeddings from the langchain library to create a vector base from the text chunks using the FAISS vector store.

5. The Language Learning Model Server (LLMS) from the langchain library is utilized to load a question-answering chain of your choice. This chain is responsible for providing answers to the user's questions based on the vectorized documents and the input question.

6. Click the "Submit" button or press Enter to get the answer to your question. The response is obtained by running the question-answering chain on the vectorized documents and the user's question.

## Dependencies

Required dependencies can be found in the requirements.txt file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.    
   
