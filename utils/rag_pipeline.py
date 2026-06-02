import os
from dotenv import load_dotenv
from groq import Groq
import chromadb
from chromadb.utils import embedding_functions

load_dotenv()

CRISIS_KEYWORDS = [
    "suicide", "kill myself", "end my life", "want to die",
    "hurt myself", "self harm", "no reason to live", "hopeless"
]

CRISIS_RESPONSE = """
I'm really concerned about what you've shared. Please know that you are not alone.

🆘 **Immediate Help Available 24/7:**
- **988 Suicide & Crisis Lifeline**: Call or text **988**
- **Crisis Text Line**: Text **HOME** to **741741**
- **Emergency**: Call **911**

Please reach out to one of these resources right now.
"""

def is_crisis(text):
    return any(keyword in text.lower() for keyword in CRISIS_KEYWORDS)

def load_knowledge_base():
    with open("data/knowledge_base.txt", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Split into chunks
    chunks = []
    sections = content.split("\n\n")
    for section in sections:
        if len(section.strip()) > 50:
            chunks.append(section.strip())
    return chunks

def setup_vectorstore(chunks):
    client = chromadb.PersistentClient(path="chroma_db")
    
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Collection already exists check
    try:
        collection = client.get_collection("mindease", embedding_function=ef)
        print("✅ Loaded existing vector database!")
    except:
        collection = client.create_collection("mindease", embedding_function=ef)
        ids = [f"chunk_{i}" for i in range(len(chunks))]
        collection.add(documents=chunks, ids=ids)
        print(f"✅ Created vector database with {len(chunks)} chunks!")
    
    return collection

def get_relevant_context(collection, query, n_results=3):
    results = collection.query(query_texts=[query], n_results=n_results)
    context = "\n\n".join(results["documents"][0])
    return context

def get_response(collection, groq_client, user_message):
    if is_crisis(user_message):
        return CRISIS_RESPONSE, True
    
    context = get_relevant_context(collection, user_message)
    
    prompt = f"""You are MindEase, a compassionate AI mental health support assistant.
Use the context below to provide empathetic, helpful support.
Never diagnose or prescribe. Always encourage professional help when needed.
Keep response to 3-4 sentences.

Context:
{context}

User: {user_message}

Compassionate response:"""

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    return response.choices[0].message.content, False

def initialize():
    chunks = load_knowledge_base()
    collection = setup_vectorstore(chunks)
    groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    return collection, groq_client

if __name__ == "__main__":
    print("Initializing MindEase...\n")
    collection, groq_client = initialize()
    
    tests = [
        "I feel very anxious lately",
        "I can't sleep at night",
        "I feel really stressed about exams"
    ]
    
    for msg in tests:
        print(f"User: {msg}")
        response, crisis = get_response(collection, groq_client, msg)
        print(f"MindEase: {response}\n")
        print("-" * 50)