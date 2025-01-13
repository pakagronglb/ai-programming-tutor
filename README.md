# 🤖 AI Programming Tutor

An interactive AI-powered programming tutor built with Streamlit and OpenAI. This application helps users learn programming through personalized chat interactions, quizzes, structured roadmaps, and curated resources.

## 🌟 Features

### 💬 Interactive Chat
- Real-time conversations with an AI tutor
- Personalized learning assistance
- Code explanations and examples
- Instant answers to programming questions

### 🧪 Interactive Quizzes
- Multiple difficulty levels
- Various programming topics
- Immediate feedback
- Progress tracking
- Detailed explanations for answers

### 🗺️ Learning Roadmap
- Structured learning paths
- Progressive difficulty levels:
  - 🌱 Beginner Path
  - 🚀 Intermediate Path
  - 💫 Advanced Path
- Project-based learning suggestions
- Customized learning tracks

### 📚 Learning Resources
- Curated programming resources
- Official documentation links
- Free online courses
- Practice platforms
- Topic-specific learning materials

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI Integration**: OpenAI GPT
- **Database**: MongoDB Atlas
- **Additional Libraries**:
  - sentence_transformers
  - pymongo
  - pydantic
  - python-dotenv

## 📋 Prerequisites

- Python 3.10 or higher
- MongoDB Atlas account
- OpenAI API key
- Git

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-programming-tutor.git
cd ai-programming-tutor
```

2. Create and activate virtual environment:
```bash
bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with:
```
MONGO_PWD=your_mongodb_password
MONGO_USER=your_mongodb_username
OPENAI_API_KEY=your_openai_api_key
```

## 🚀 Running the Application

1. Start the application:
```bash
streamlit run Home.py
```

2. Open your browser and navigate to:
```
http://localhost:8501
```

## 📁 Project Structure

```
ai-programming-tutor/
├── Home.py                 # Main application file
├── requirements.txt        # Project dependencies
├── README.md              # Project documentation
├── .env                   # Environment variables
├── .gitignore            # Git ignore file
├── components/           # Application components
│   ├── chat.py          # Chat functionality
│   ├── quiz.py          # Quiz system
│   └── resources.py     # Learning resources
├── database.py           # Database operations
└── models.py            # Data models
```

## 🔧 Configuration

### MongoDB Setup
1. Create a MongoDB Atlas account
2. Create a new cluster
3. Set up database access
4. Whitelist your IP address
5. Get your connection string

### OpenAI Setup
1. Create an OpenAI account
2. Generate an API key
3. Add the key to your environment variables

## 🚀 Deployment

The application can be deployed on Streamlit Cloud:

1. Push code to GitHub
2. Connect to Streamlit Cloud
3. Configure secrets in Streamlit Cloud dashboard
4. Deploy the application

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- OpenAI for the GPT API
- Streamlit for the wonderful framework
- MongoDB for the database solution
- All contributors and users of this project

## 📞 Support

For support, email pakagronglebel@gmail.com or open an issue in the GitHub repository.
```

