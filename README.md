# Chatbot Using HugChat

This project demonstrates how to create a simple chatbot using the HugChat library and Streamlit for the user interface. The chatbot allows users to log in with their Hugging Face credentials and interact with the AI model to get responses to their queries.

## Features

- **User Authentication:** Users can log in using their Hugging Face email and password.
- **Chat Interface:** After successful login, users can enter their prompts and receive responses from the chatbot.
- **State Management:** Maintains session state to keep track of the conversation history.

## Screenshots

![Screenshot](/images/demo01.png)

## Installation

To run this project, you need to have Python installed on your system. Follow the steps below to set up and run the project.

### Prerequisites

- Python 3.7 or higher
- Streamlit
- HugChat library

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/nguyenhads/hugchat_app.git
   cd hugchat_app
   ```

2. **Create virtual envs and Install the required packages:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate # Activate your virtual env
   pip install streamlit hugchat
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Login:**

   - Open the web application.
   - Enter your Hugging Face email and password in the sidebar.
   - Click the "Login" button.

2. **Chat:**
   - Once logged in, you can start typing your prompts in the chat input field at the bottom.
   - The chatbot will respond to your queries, and the conversation will be displayed in the main area.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
