import streamlit as st
from huggingface_hub import InferenceClient
from io import BytesIO
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }

    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        font-size: 16px;
    }

    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3rem;
        font-size: 18px;
        font-weight: bold;
        transition: all 0.3s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }

    .generated-image {
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🎨 AI Image Generator</h1>
    <p style="font-size: 1.2rem; margin: 0; opacity: 0.9;">Stable Diffusion XL | Raw Model Output</p>
</div>
""", unsafe_allow_html=True)


# Initialize client
@st.cache_resource
def get_client():
    return InferenceClient(
        provider="nebius",
        api_key="YOUR_API_KEY",
    )




client = get_client()

# Create layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📝 Enter Your Prompt")

    # Prompt input (replacing input())
    promptt = st.text_area(
        "Describe your image:",
        placeholder="A beautiful sunset over mountains...",
        height=150,
        key="prompt_input"
    )

    # Generate button
    generate_clicked = st.button("🎨 Generate Image", type="primary")

    # Model info
    st.markdown("---")
    st.info("🤖 **Model**: Stable Diffusion XL Base 1.0\n🏢 **Provider**: Nebius")

with col2:
    st.markdown("### 🖼️ Generated Image")

    # Generate and display image
    if generate_clicked and promptt:
        with st.spinner("🎨 Generating your image..."):
            try:
                # Original logic - no modifications
                image = client.text_to_image(
                    promptt,
                    model="stabilityai/stable-diffusion-xl-base-1.0",
                )

                # Display image (replacing plt.imshow/plt.show)
                st.image(image, caption=f"Generated: {promptt}", use_column_width=True)

                # Success message
                st.success("✅ Image generated successfully!")

                # Store in session state for persistence
                st.session_state.generated_image = image
                st.session_state.current_prompt = promptt

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

    # Display stored image if exists
    elif hasattr(st.session_state, 'generated_image'):
        st.image(
            st.session_state.generated_image,
            caption=f"Generated: {st.session_state.current_prompt}",
            use_column_width=True
        )

    else:
        # Placeholder
        st.markdown("""
        <div style="
            height: 400px; 
            border: 2px dashed #cccccc; 
            border-radius: 15px; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            background: #f8f9fa;
            color: #666;
            font-size: 1.2rem;
        ">
            🖼️ Your generated image will appear here
        </div>
        """, unsafe_allow_html=True)

# Download section
if hasattr(st.session_state, 'generated_image'):
    st.markdown("---")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        # Convert image to downloadable format
        img_buffer = BytesIO()
        st.session_state.generated_image.save(img_buffer, format='PNG')
        img_buffer.seek(0)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sdxl_image_{timestamp}.png"

        st.download_button(
            label="📥 Download Image",
            data=img_buffer.getvalue(),
            file_name=filename,
            mime="image/png",
            use_container_width=True
        )

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem; color: #666; font-size: 14px;">
    🤖 Raw Stable Diffusion XL Output | No Prompt Modifications
</div>
""", unsafe_allow_html=True)
