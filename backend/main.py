from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import tempfile
import logging
from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Import from local modules
try:
    from models.vector_store import VectorStore
    from services.storage_service import S3Storage
    from services.llm_service import LLMService
    from config import Config
except ImportError:
    from .models.vector_store import VectorStore
    from .services.storage_service import S3Storage
    from .services.llm_service import LLMService
    from .config import Config

app = Flask(__name__)
CORS(app)

# Initialize services
vector_store = VectorStore(Config.VECTOR_DB_PATH)
storage_service = S3Storage()
llm_service = LLMService(vector_store)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process_document(file):
    temp_dir = tempfile.mkdtemp()
    temp_path = os.path.join(temp_dir, file.filename)
    try:
        file.save(temp_path)
        if file.filename.endswith('.pdf'):
            loader = PyPDFLoader(temp_path)
        else:
            loader = TextLoader(temp_path)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        return text_splitter.split_documents(documents)
    finally:
        if os.path.exists(temp_path): os.remove(temp_path)
        os.rmdir(temp_dir)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    if not data or 'question' not in data:
        return jsonify({'error': 'No question provided'}), 400
    try:
        response = llm_service.get_response(data['question'])
        return jsonify({'answer': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/upload', methods=['POST'])
def upload_document():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    try:
        text_chunks = process_document(file)
        storage_service.upload_file(file, file.filename)
        vector_store.add_documents(text_chunks)
        return jsonify({'message': 'Success', 'chunks': len(text_chunks)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)