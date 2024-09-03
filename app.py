import streamlit as st
from src.textsummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline



class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        
    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained('tokenizer')
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        pipe = pipeline("summarization", model='pegasus-samsum-model',tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output





def main():
    # Set page config
    st.set_page_config(page_title="Dialogue Summarizer", page_icon="💬", layout="wide")

    # Custom CSS to improve the appearance
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    .result-font {
        font-size:18px !important;
        font-style: italic;
    }
    .stButton>button {
        width: 100%;
        height: 50px;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # App title and description
    st.title("🤖 AI Dialogue Summarizer")
    st.markdown("Transform your lengthy conversations into concise summaries with our cutting-edge AI technology.")

    # Create two columns
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<p class="big-font">Input Dialogue</p>', unsafe_allow_html=True)
        user_input = st.text_area("", height=300, placeholder="Paste your dialogue here...")

    with col2:
        st.markdown('<p class="big-font">Summary</p>', unsafe_allow_html=True)
        summary_placeholder = st.empty()

    # Create an instance of PredictionPipeline
    predictor = PredictionPipeline()

    if st.button("📝 Generate Summary"):
        if user_input:
            with st.spinner('Generating summary...'):
                # Get the summary
                summary = predictor.predict(user_input)
                # Display the summary
                summary_placeholder.markdown(f'<p class="result-font">{summary}</p>', unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter some text to summarize.")

    # Add some spacing
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Add a section for app info
    st.markdown("## About This App")
    st.info("""
    This AI-powered dialogue summarizer uses advanced natural language processing to distill the key points from conversations. 
    It's perfect for quickly understanding the essence of meetings, chats, or any form of dialogue.
    
    **How to use:**
    1. Paste your dialogue in the text area on the left.
    2. Click the 'Generate Summary' button.
    3. View the AI-generated summary on the right.
    
    For best results, ensure your input is a clear dialogue or conversation.
    """)

if __name__ == "__main__":
    main()