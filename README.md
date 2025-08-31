# 🎨 AI Image Generator

A simple and elegant Streamlit web application for generating high-quality images using Stable Diffusion XL via Hugging Face's Nebius provider.

## ✨ Features

- **Raw Model Output**: Pure Stable Diffusion XL results with no prompt modifications
- **High Quality**: Generates 1024x1024 resolution images
- **Clean Interface**: Simple and intuitive web-based UI
- **Direct Download**: Save generated images as PNG files
- **Session Persistence**: Images remain visible until you generate new ones
- **Real-time Generation**: Watch your images being created in real-time

## 🚀 Quick Start

### Prerequisites

Make sure you have Python 3.7+ installed, then install the required packages:

```bash
pip install streamlit huggingface-hub pillow
```

### Installation

1. Clone or download this repository
2. Save the main code as `app.py`
3. Run the application:

```bash
streamlit run app.py
```

4. Open your browser to `http://localhost:8501`

## 🎯 How to Use

1. **Enter Your Prompt**: Describe the image you want to generate in the text area
2. **Click Generate**: Press the "Generate Image" button
3. **View Result**: Your image will appear on the right side
4. **Download**: Click the download button to save your image

### Example Prompts

- `A serene mountain landscape at sunset`
- `Portrait of a wise old wizard`
- `Futuristic cityscape with flying cars`
- `Abstract geometric patterns in blue and gold`
- `A cute robot sitting in a garden`

## 🔧 Technical Details

### Model Information
- **Model**: `stabilityai/stable-diffusion-xl-base-1.0`
- **Provider**: Nebius (via Hugging Face)
- **Resolution**: 1024x1024 pixels
- **Format**: PNG

### API Configuration
The app uses a pre-configured Hugging Face API key for the Nebius provider. The client is initialized as:

```python
client = InferenceClient(
    provider="nebius",
    api_key="YOUR_API_KEY",
)
```

## 📁 Project Structure

```
ai-image-generator/
│
├── app.py              # Main Streamlit application
├── README.md           # This file
└── requirements.txt    # Python dependencies (optional)
```

## 📦 Dependencies

- `streamlit` - Web application framework
- `huggingface-hub` - Hugging Face API client
- `pillow` - Image processing library

Create a `requirements.txt` file with:

```
streamlit
huggingface-hub
pillow
```

## 🛠️ Customization

### Changing the Model
To use a different model, modify the model parameter in the `text_to_image` call:

```python
image = client.text_to_image(
    promptt,
    model="your-preferred-model",  # Change this
)
```

### Adding Multiple Images
To generate multiple images, wrap the generation logic in a loop:

```python
for i in range(num_images):
    image = client.text_to_image(promptt, model="...")
```

### Custom Styling
The app includes custom CSS in the `st.markdown()` sections. Modify these to change the appearance.

## ⚠️ Troubleshooting

### Common Issues

**"Connection Error"**
- Check your internet connection
- Verify the API key is valid
- Try again in a few moments

**"Model Loading Error"**
- The model might be initializing, wait 30-60 seconds and try again
- Try a simpler prompt first

**"Rate Limit Exceeded"**
- Wait a few minutes between generations
- The free tier has usage limits

### Error Messages
The app provides detailed error messages in the Streamlit interface. Check the browser console or terminal for additional debugging information.

## 🤝 Contributing

This is a simple educational project. Feel free to:

1. Fork the repository
2. Add new features or models
3. Improve the UI/UX
4. Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Stability AI** for the Stable Diffusion XL model
- **Hugging Face** for the inference API and Nebius provider
- **Streamlit** for the amazing web app framework

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify your dependencies are correctly installed
3. Ensure you have a stable internet connection
4. Try with simpler prompts first

---
