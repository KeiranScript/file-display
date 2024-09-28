import os
from flask import Flask, render_template_string, redirect, url_for
from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import HtmlFormatter
from custom_style import CustomStyle

app = Flask(__name__)

# Directory where files are stored
FILES_DIR = "files"


@app.route("/")
def index():
    return redirect(url_for("files_list"))


@app.route("/files")
def files_list():
    # List all files in the /files directory
    files = os.listdir(FILES_DIR)
    return render_template_string(FILES_TEMPLATE, files=files)


@app.route("/file/<filename>")
def display_file(filename):
    file_path = os.path.join(FILES_DIR, filename)

    if not os.path.isfile(file_path):
        return "File not found!", 404

    with open(file_path, "r") as file:
        file_content = file.read()

    # Determine the lexer based on the file extension
    lexer = get_lexer_for_filename(filename)
    formatter = HtmlFormatter(style=CustomStyle)

    # Highlight the code
    highlighted_content = highlight(file_content, lexer, formatter)
    style = formatter.get_style_defs()

    return render_template_string(
        HTML_TEMPLATE, content=highlighted_content, style=style, filename=filename
    )


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ filename }}</title>
    <style>
        body {
            background-color: #121212;
            color: #e0e0e0;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: #1e1e1e;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
            animation: fadeIn 0.5s ease;
            max-width: 600px;
            overflow: auto;
            text-align: left; /* Align text to the left for the code content */
        }
        h1 {
            margin-bottom: 20px;
            text-align: center; /* Center align the header */
        }
        pre {
            white-space: pre-wrap; /* Allows long lines to wrap */
            word-wrap: break-word; /* Breaks long words */
            margin: 0; /* Remove default margin */
            padding: 10px; /* Add padding for better readability */
            background-color: #282828; /* Background color for the code */
            border-radius: 5px; /* Rounded corners for the code block */
        }
        .button-container {
            display: flex;
            justify-content: center; /* Center the buttons horizontally */
            margin-top: 20px; /* Spacing above the button container */
        }
        button {
            background-color: #64b5f6; /* Nice shade of blue */
            color: #ffffff;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
            font-size: 16px;
            margin: 0 10px; /* Spacing between buttons */
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #1e88e5; /* Darker blue on hover */
        }
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
        {{ style | safe }} /* Inject the Pygments style */
    </style>
    <script>
        function copyToClipboard() {
            // Create a temporary textarea element
            const textArea = document.createElement('textarea');
            textArea.value = document.getElementById('file-content').innerText;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            alert('File content copied to clipboard!');
        }
    </script>
</head>
<body>
    <div class="container">
        <h1>{{ filename }}</h1>
        <div id="file-content" class="highlight"><pre>{{ content | safe }}</pre></div>
        <div class="button-container">
            <button onclick="copyToClipboard()">Copy</button>
            <a href="{{ url_for('files_list') }}">
                <button>Back</button>
            </a>
        </div>
    </div>
</body>
</html>
"""

FILES_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File List</title>
    <style>
        body {
            background-color: #121212;
            color: #e0e0e0;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 20px;
        }
        h1 {
            text-align: center;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 10px 0;
            text-align: center;
        }
        a {
            color: #64b5f6;
            text-decoration: none;
            transition: color 0.3s;
        }
        a:hover {
            color: #1e88e5;
        }
    </style>
</head>
<body>
    <h1>Select a File to View</h1>
    <ul>
        {% for file in files %}
            <li><a href="{{ url_for('display_file', filename=file) }}">{{ file }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
