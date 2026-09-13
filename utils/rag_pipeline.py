import os
from dotenv import load_dotenv
from groq import Groq

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
    chunks = [s.strip() for s in content.split("\n\n") if len(s.strip()) > 50]
    return chunks

def get_relevant_context(chunks, query, n=3):
    """Simple keyword-based retrieval — ChromaDB అక్కర్లేదు!"""
    query_words = set(query.lower().split())
    scored = []
    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        score = len(query_words & chunk_words)
        scored.append((score, chunk))
    scored.sort(reverse=True)
    return "\n\n".join([c for _, c in scored[:n]])

def initialize():
    chunks = load_knowledge_base()
    groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    print(f"✅ Loaded {len(chunks)} knowledge chunks!")
    return chunks, groq_client

def get_response(chunks, groq_client, user_message):
    if is_crisis(user_message):
        return CRISIS_RESPONSE, True

    context = get_relevant_context(chunks, user_message)

    prompt = f"""You are MindEase, a compassionate AI mental health support assistant.
Use the context below to provide empathetic, helpful support.
Never diagnose or prescribe. Always encourage professional help when needed.
Keep response to 3-4 sentences.

Context:
{context}

User: {user_message}

Compassionate response:"""

    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content, False