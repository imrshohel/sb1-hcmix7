# AI Proofreading Tool

An AI-assisted desktop application for proofreading and improving content.

## Features

- Document management (create, edit, delete)
- AI-powered suggestions for grammar and style improvements
- Multiple AI service integrations (OpenAI, Claude, Google AI, Groq, Ollama)
- Customizable prompts

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-proofreading-tool.git
   cd ai-proofreading-tool
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```
   python ai_proofreading_tool/init_db.py
   ```

## Usage

Run the application:
```
python ai_proofreading_tool/main.py
```

## Configuration

- API keys for AI services should be set in the Settings panel of the application.
- Custom prompts can be created and modified in the Settings panel.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.