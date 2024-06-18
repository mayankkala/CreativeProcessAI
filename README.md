# AI-Driven Creative Process Information Retrieval System

This project leverages the LangChain framework to build an AI-driven system that retrieves and summarizes information on the creative process from various sources. It integrates the Chroma vector store for efficient document retrieval and uses the Groq API for generating responses.

## Features

- **WebBaseLoader**: Fetches relevant documents from specified URLs.
- **Chroma Vector Store**: Utilizes Chroma for storing document vectors and quick information retrieval.
- **OpenAI Embeddings**: Embeds documents for vector storage and retrieval.
- **Groq API**: Uses the Groq API for generating responses.
- **Streamlit**: Provides a user-friendly interface for interacting with the system.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Streamlit

### Steps

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/creative-process-info-retrieval.git
    cd creative-process-info-retrieval
    ```

2. **Create and Activate Virtual Environment**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up API Keys**

    Create a `.env` file in the root directory and add your Groq API key:

    ```plaintext
    GROQ_API_KEY=your_groq_api_key
    ```

## Usage

1. **Run the Application**

    ```sh
    streamlit run app.py
    ```

2. **Interacting with the System**

    - Input your query related to the creative process.
    - The system will retrieve and summarize information from the specified web sources.

## Project Structure

- `app.py`: Main application file to run the Streamlit app.
- `requirements.txt`: List of required Python packages.
- `.env`: File to store environment variables, such as API keys.
- `README.md`: This file.
```

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License

This project is licensed under the MIT License.



For any questions or suggestions, please open an issue or contact [yourname](mailto:youremail@example.com).

Thank you for using our AI-Driven Creative Process Information Retrieval System!

---

Feel free to modify the content according to your specific project details and structure.
