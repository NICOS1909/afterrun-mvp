# AfterRun – Dein Laufcoach (MVP)

A Streamlit-based web application that helps runners analyze their activities and receive structured feedback.

## 🎯 Overview

AfterRun is a minimal viable product (MVP) that allows users to:
- Upload running activity files (GPX or TCX format)
- Complete a brief self-assessment questionnaire (3 questions)
- Receive structured AI-generated feedback including:
  - Activity summary
  - Context analysis
  - Comparison between objective data and subjective feelings
  - Reflection questions for personal growth

**Note:** This app provides informational feedback only. It does not create training plans or provide medical advice.

## 🏗️ Project Structure

```
afterrun-mvp/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env.example               # Environment configuration template
├── data/
│   └── uploads/               # Directory for uploaded activity files
└── src/
    ├── models/
    │   ├── __init__.py
    │   └── activity.py        # Data models (ActivityData, SelfAssessment, Feedback)
    ├── services/
    │   ├── __init__.py
    │   ├── file_parser.py     # GPX/TCX file parsing service
    │   └── ai_feedback.py     # AI feedback generation service (placeholder logic)
    └── utils/
        ├── __init__.py
        └── file_utils.py      # File operation utilities
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/NICOS1909/afterrun-mvp.git
cd afterrun-mvp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Configure environment variables:
```bash
cp .env.example .env
# Edit .env as needed
```

### Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 📖 Usage

1. **Upload Activity**: Click on the file uploader and select a GPX or TCX file from your running watch or fitness app.

2. **View Activity Summary**: After upload, you'll see key metrics from your run (distance, duration, pace, etc.).

3. **Complete Self-Assessment**: Answer three questions about your run:
   - How did you feel during the run?
   - How hard was the run for you?
   - Any additional notes (optional)

4. **Receive Feedback**: Click "Feedback generieren" to get structured feedback including:
   - Summary of your run
   - Context about distance and pace
   - Analysis comparing your data with your feelings
   - Reflection questions to help you grow as a runner

5. **Start New Analysis**: Click "Neue Analyse starten" to analyze another run.

## 🛠️ Technical Details

### Key Dependencies

- **streamlit**: Web application framework
- **gpxpy**: GPX file parsing
- **python-tcxparser**: TCX file parsing
- **python-dotenv**: Environment variable management

### Data Models

- **ActivityData**: Stores parsed activity metrics (distance, pace, heart rate, etc.)
- **SelfAssessment**: Stores user's self-assessment responses
- **Feedback**: Stores structured AI feedback components

### Services

- **FileParserService**: Parses GPX and TCX files to extract activity data
- **AIFeedbackService**: Generates structured feedback (currently using placeholder logic)

## 🔮 Future Enhancements

- Integration with actual AI/LLM services (OpenAI, Anthropic, etc.)
- Support for more file formats (FIT, etc.)
- User accounts and activity history
- Progress tracking over time
- Export feedback as PDF
- Multi-language support

## ⚠️ Limitations

- This is an MVP with placeholder AI logic
- No training plan generation
- No medical advice provided
- Files are stored locally and cleaned up after 7 days
- No user authentication

## 📝 License

This project is provided as-is for demonstration purposes.

## 🤝 Contributing

This is an MVP project. Contributions, issues, and feature requests are welcome!

## 👤 Author

NICOS1909
