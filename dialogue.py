import streamlit as st
import google.generativeai as genai

# Directly set your API Key
GOOGLE_API_KEY = ''  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Model
model = genai.GenerativeModel('gemini-1.5-flash')

# Streamlit application title
st.title("Smart English Assistant")

# Instructions for the user
st.markdown("""
### Instructions:
1. **Enter a Topic**: In the text box below, type the topic you want to generate a dialogue about. 
2. **Generate Dialogue**: Click the "Generate Dialogue" button to create a dialogue based on the topic you provided.
3. **View the Result**: The generated dialogue will be displayed below the button.
4. **Try Different Topics**: Feel free to enter different topics to see various dialogues!
""")

# User input for the topic of dialogue
dialogue_topic = st.text_input("Enter the topic for the dialogue:")

# Button to generate dialogue
if st.button("Generate Dialogue") and dialogue_topic:
    try:
        # Generate dialogue based on the topic
        prompt = f"Generate a dialogue about '{dialogue_topic}'"

        # Generate Content
        response = model.generate_content(prompt, stream=True)

        # Display the Response
        st.subheader("Generated Dialogue:")
        for res in response:
            st.markdown(res.text)
    except Exception as e:
        st.error(f"An error occurred while generating the dialogue: {e}")
else:
    st.warning("Please enter a topic to generate a dialogue.")
