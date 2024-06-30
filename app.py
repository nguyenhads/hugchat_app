import streamlit as st
from hugchat import hugchat
from hugchat.login import Login


def login(email, password):
    """
    Attempt to login to HugChat with the provided email and password.

    Parameters:
    email (str): Hugging Face email.
    password (str): Hugging Face password.

    Returns:
    tuple: (bool, object/str) - True and cookies if successful, False and error message if not.
    """
    try:
        sign = Login(email=email, passwd=password)
        cookies = sign.login()
        # Thử yêu cầu đơn giản để kiểm tra đăng nhập
        client = hugchat.ChatBot(cookies=cookies.get_dict())
        response = client.chat("Who am I")
        if response:
            return True, cookies
        else:
            return False, "Login failed. User information does not match."
    except Exception as e:
        return False, str(e)


def generate_response(prompt_input, cookies):
    """
    Generate a response from the ChatBot using the given prompt.

    Parameters:
    prompt_input (str): The user's prompt.
    cookies (object): Cookies obtained from successful login.

    Returns:
    str: The response from the ChatBot.
    """
    # Create ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)


def main():
    """
    Main function to run the Streamlit app.
    """
    st.title("Simple Chatbot Using Hugchat💬")

    # Hugging Face Credentials
    with st.sidebar:
        st.title("Login HugChat")
        hf_email = st.text_input("Hugging Face Email: ")
        hf_password = st.text_input("Password:", type="password")
        login_button = st.button("Login")

        if login_button:
            if not (hf_email and hf_password):
                st.warning(
                    "Please enter your Hugging Face email and password correctly",
                    icon="⚠️",
                )
            else:
                login_success, login_data = login(hf_email, hf_password)
                if login_success:
                    st.session_state["login_cookies"] = login_data
                    st.session_state["logged_in"] = True
                    st.write("Login successful !")
                    st.success("Proceed to entering your prompt message!", icon="👉")
                else:
                    st.error(
                        f"Cannot login! Please confirm your account is correct: {login_data}",
                        icon="⚠️",
                    )

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "How may I help you?"}
        ]

    if "logged_in" in st.session_state and st.session_state["logged_in"]:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        if prompt := st.chat_input("Type your message here..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)

            # Generate a new response if last message is not from assistant
            if st.session_state.messages[-1]["role"] != "assistant":
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        response = generate_response(
                            prompt, st.session_state["login_cookies"]
                        )
                        st.write(response)
                message = {"role": "assistant", "content": response}
                st.session_state.messages.append(message)
    else:
        st.info("Please login to start chatting.")


if __name__ == "__main__":
    main()
