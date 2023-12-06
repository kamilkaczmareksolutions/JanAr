# JanAr - Automated Social Media Caption Generator for Artworks

## Introduction
JanAr is a specialized GUI application designed to automatically generate social media captions for artwork images. By leveraging the power of GPT-4-Vision and other GPT models, JanAr provides unique, engaging captions that combine artistic insight with social media engagement strategies. This tool is specifically tailored for my friend's glass workshop and picture framing business, transforming photographs of artworks into captivating stories and descriptions.

## Why Use JanAr?
- **Highly Tailored Solution**: Custom-built for generating captions that reflect the essence and beauty of artworks, while also engaging the audience.
- **Streamlined Social Media Management**: Simplifies the content creation process for social media, especially for my friend who finds writing captions time-consuming.
- **Balanced Descriptions**: Combines artistic description with online engagement techniques, delivering captions that are informative and appealing.
- **Password-Protected Access**: Ensures exclusive usage with API key protection, making it a personalized tool for the business.

## Key Features
- **Dual AI-Powered Approach**: Utilizes GPT-4-Vision for artistic interpretation and other GPT model for audience engagement in captions.
- **Customizable Input Options**: My friend can upload artwork images and optionally add brief description or keywords (like: "Mrs. Kasia brought us this painting, she wanted us to frame it for her daughter").
- **Streamlit-Based Simple UI**: User-friendly interface that's easy to navigate and use.
![Streamlit-UI-screenshot](https://github.com/kamilkaczmareksolutions/JanAr/assets/95218485/9a7a593d-d899-4c5d-8130-0ef056fb072b)

- **Secure and Private**: Password-protected access to maintain exclusivity and security.

![password-protection-screenshot](https://github.com/kamilkaczmareksolutions/JanAr/assets/95218485/a174fd6d-4815-40a4-befe-b89a45d2f74e)

## Technologies Used
- **Python**: The core language for backend development.
- **OpenAI GPT Models**: GPT-4-Vision for visual interpretation and other GPT for textual content generation.
- **Streamlit**: For creating the web-based user interface.

## How It Works
1. **Image and Optional Text Input**:
   - User upload an image of the artwork and can optionally add a few words about it, but he don't have to.
2. **AI-Driven Caption Generation**:
   - GPT-4-Vision model describes the artistic elements of the image.
   - Model of choice (usually GPT-4-Vision as well, but might be e.g. 3.5-Turbo) creates a social-media-friendly caption based on the image description and information about the business embedded in the system prompt AND optional user input.
3. **Combining Outputs**:
   - The application intelligently merges outputs from both models to form a well-balanced caption.

## Usage
A demonstration GIF showcasing the entire process from image upload to caption generation.

![Usage GIF](https://github.com/kamilkaczmareksolutions/JanAr/assets/95218485/c49f2c10-89f5-4b30-ab3f-fbb5b2231939)

## Contributing
While JanAr is tailored for a specific use case, contributions are welcome. Feel free to fork the repository, and do whatever you want with it. Maybe you want to play a bit with GPT-4-Vision? :)

## Notes
- JanAr is ideal solution for my friend to boost his online presence with minimal effort in content creation.
- The tool is currently designed for a specific business but can be adapted with changes in the prompts and .env file configuration, if someone wants to play with it.
