import os
import tempfile
from flask import Flask, request, jsonify
from ollama import chat
from PyPDF2 import PdfReader
import json

app = Flask(__name__)

def parse_resume(file_path, jd):
    with open(file_path, 'rb') as file:
        pdf_text = ""
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()

    response = chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': 'Given a job description - {' + jd + '} and a resume - {' + pdf_text + '}, Provide resume match percentage in json format as output example like {"resume_match_percentage": "percentage"}.',
        },
    ])

    # Instead of returning the raw response, we parse it here and return a structured JSON
    parsed_data = parse_ollama_response(response['message']['content'])
    return jsonify(parsed_data)

def parse_ollama_response(ollama_response):
    # Find the JSON string within the Ollama response
    start_index = ollama_response.find('{')
    end_index = ollama_response.rfind('}')

    if start_index != -1 and end_index != -1:
        json_string = ollama_response[start_index:end_index+1]
        try:
            parsed_data = json.loads(json_string)
            return parsed_data  # Return the parsed data directly
        except json.JSONDecodeError:
            return {'error': 'Invalid JSON response from Ollama'}
    else:
        return {'error': 'No JSON data found in the response'}

@app.route('/parse_resume', methods=['POST'])
def handle_parse_resume():
    # Assuming the PDF file is sent as form data in the request
    file = request.files['resume']
    jd = request.form['jd']
    _, file_extension = os.path.splitext(file.filename)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=file_extension)
    file.save(temp_file.name)

    # Parse the resume and return the structured JSON
    json_output = parse_resume(temp_file.name,jd)
    
    # Clean up - close and delete the temporary file
    temp_file.close()
    os.unlink(temp_file.name)

    return json_output

if __name__ == "__main__":
    app.run(debug=True)
