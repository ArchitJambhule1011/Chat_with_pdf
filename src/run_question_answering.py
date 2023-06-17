from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

def run_question_answering(user_q, vector_base):
    docs = vector_base.similarity_search(user_q)
    llm = OpenAI()
    chain = load_qa_chain(llm, chain_type='stuff')
    response = chain.run(input_documents=docs, question=user_q)
    return response