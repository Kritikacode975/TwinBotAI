# Gemini LLM Q&A Application

This repository contains a Streamlit application that interacts with the Gemini Pro Large Language Model (LLM) for a Question & Answer demo. The application uses `google.generativeai` for interacting with the Gemini Pro model and provides real-time responses to user queries.

## Features

- **Streamlit UI**: A simple and user-friendly interface to interact with the Gemini Pro model.
- **Real-Time Q&A**: Users can input queries and receive responses from the Gemini Pro LLM.
- **Chat History**: Maintains the history of conversations within the session.

## Prerequisites

- Python 3.7+
- A Google API Key with access to the Gemini Pro LLM.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/gemini-llm-demo.git
   cd gemini-llm-demo
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Google API Key:

   ```env
   GOOGLE_API_KEY=your-google-api-key
   ```

## Usage

1. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

2. Open the provided URL in your browser (e.g., `http://localhost:8501`).

3. Input your query in the text box and click the "Ask the question" button to get a response from the Gemini Pro model.

## File Structure

- `app.py`: The main application file.
- `.env`: Contains environment variables (not included in the repo, must be created).
- `requirements.txt`: Lists the dependencies required to run the application.

## How It Works

1. The application initializes the Gemini Pro model using the `google.generativeai` library.
2. Users input their queries through the Streamlit interface.
3. The application sends the query to the Gemini Pro model and streams the response back in real-time.
4. Both the user's query and the model's response are stored and displayed as chat history.


---

Feel free to contribute or open issues if you encounter any problems!
