<h1>Local Flask API for Resume Parsing with Ollama and Llama3</h1>

<p>This project is a local Flask API designed to parse resumes using Ollama and Llama3. It allows for extracting key information from resumes, making it easier to analyze and process candidate data.</p>
<h2>Features</h2>
    <ul>
        <li><strong>Resume Parsing:</strong> Extracts key information such as name, contact details, work experience, education, and skills from resumes.</li>
        <li><strong>Integration with Ollama and Llama3:</strong> Utilizes the advanced capabilities of Ollama and Llama3 for accurate and efficient parsing.</li>
        <li><strong>Simple API Interface:</strong> Provides a straightforward RESTful API for parsing resumes locally.</li>
    </ul>

<h2>Prerequisites</h2>
    <ul>
        <li>Python 3.8+</li>
        <li>Flask</li>
        <li>Ollama and Llama3 libraries</li>
    </ul>

<h2>Installation</h2>
    <ol>
        <li><strong>Clone the repository:</strong>
            <pre><code>git clone https://github.com/neelshrimali/ollama-resumeparser.git
cd ollama-resumeparser</code></pre>
        </li>
        <li><strong>Create and activate a virtual environment:</strong>
            <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
        </li>
        <li><strong>Install the dependencies:</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
    </ol>

<h2>Usage</h2>
    <ol>
        <li><strong>Start the Flask API:</strong>
            <pre><code>flask run</code></pre>
        </li>
        <li><strong>Send a POST request to parse a resume:</strong>
            <p>Endpoint: <code>/api/parse-resume</code></p>
            <p>Example request:</p>
            <pre><code>curl -X POST -F 'file=@resume.pdf' http://127.0.0.1:5000/api/parse-resume</code></pre>
        </li>
        <li><strong>Receive the parsed data:</strong>
            <p>The API will return a JSON response with the extracted information.</p>
        </li>
    </ol>
