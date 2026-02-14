# 🏦 Banking Bot

A conversational banking assistant powered by **Mistral AI's largest model** with a **Streamlit** web interface.

## Features

✨ **24/7 Customer Support** - Available anytime you need banking assistance  
🤖 **Powered by Mistral-Large-Latest** - Advanced AI for intelligent conversations  
💬 **Chat Interface** - Interactive and user-friendly web application  
🔒 **Secure** - Professional-grade banking guidance  
📱 **Responsive Design** - Works on desktop and mobile browsers  

### Services Offered

- Account information and balances
- Transaction history assistance
- Money transfer guidance
- Loan information
- Credit card services
- Investment advice
- Banking fees and charges explanation
- Customer service solutions
- Financial guidance and tips

## Prerequisites

- Python 3.8 or higher
- Mistral AI API key
- pip (Python package manager)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/salihakhadher-creator/Bank-sal.git
cd Bank-sal
```

### 2. Create Virtual Environment

```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Create a `.env` file in the project root:

```bash
MISTRAL_API_KEY=your_api_key_here
```

Or copy the example file:

```bash
cp .env.example .env
```

Then add your Mistral API key to the `.env` file.

## Usage

### Run the Application

```bash
streamlit run banking_bot.py
```

The application will open in your default browser at `http://localhost:8501`

### Interacting with the Bot

1. **Type Your Question** - Use the chat input at the bottom of the screen
2. **Get Instant Response** - The bot will analyze and respond to your banking query
3. **Continue Conversation** - Ask follow-up questions naturally
4. **Clear History** - Use the "Clear Chat History" button in the sidebar to start fresh

### Sample Questions

- "What's a good savings strategy?"
- "How do I transfer money between accounts?"
- "What loan options are available?"
- "What are your banking fees?"
- "How can I improve my credit score?"
- "What's the difference between savings and checking?"
- "How do I apply for a credit card?"

## Project Structure

```
Bank-sal/
├── banking_bot.py          # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## Configuration

### Mistral AI Model

The bot uses **mistral-large-latest** model with the following settings:

- **Model**: mistral-large-latest
- **Max Tokens**: 1000
- **Temperature**: 0.7 (balanced between deterministic and creative responses)

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `MISTRAL_API_KEY` | Your Mistral AI API key | `your_api_key_here` |

## Security Notes

⚠️ **Important**: 
- Never commit `.env` files to version control
- Keep your API key confidential
- This bot provides informational guidance only
- For real account transactions or sensitive operations, contact your bank directly

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.28.1+ | Web UI framework |
| mistralai | 0.0.20+ | Mistral AI API client |
| python-dotenv | 1.0.0+ | Environment variable management |

## Troubleshooting

### Port Already in Use

If port 8501 is already in use, you can specify a different port:

```bash
streamlit run banking_bot.py --server.port 8502
```

### API Key Issues

Ensure your `.env` file is in the project root and contains:
```
MISTRAL_API_KEY=your_actual_api_key
```

### Slow Responses

- Check your internet connection
- Verify your Mistral API key is valid
- Try reducing the max_tokens parameter in the code

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

**Saliha Khadher**
- GitHub: [@salihakhadher-creator](https://github.com/salihakhadher-creator)
- Email: saliha.khadher@gmail.com

## Support

For issues, questions, or suggestions, please open an issue on the [GitHub repository](https://github.com/salihakhadher-creator/Bank-sal/issues).

## Disclaimer

This banking bot is an informational tool only. It does not perform actual banking transactions. Always consult with your bank for:
- Sensitive financial decisions
- Account modifications
- Transaction execution
- Personal financial planning

---

**Last Updated**: February 14, 2026

**Version**: 1.0.0
