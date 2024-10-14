# About HealthyHer

## Inspiration
I wanted to create a website that helps teenage girls like me develop healthy eating habits in a way that's simple and easy. These days, there is such an unhealthy focus on body image. Social media and fast food culture can promote bad eating habits and worsen this problem. According to research done at Tufts University, about 67% of adolescents suffer from poor diet. To combat this, I wanted to create a website that can help teenagers manage their food choices and make healthy decisions in a way that's not overwhelming or stressful.

## What it does
HealthyHer uses Gemini API to analyze the meal in the uploaded image and provide the calorie count and advice.

## How we built it
I built it using the VS code IDE and used Python programming. I used three libraries: streamlit, google.generativeai, and python-dotenv. Streamlit helped with the creation of the web application, google.generativeai allowed  me to access and implement Google's generative AIs, which in this case was Gemini API. Python-dotenv helped to manage my environment variables.

## Challenges we ran into
The main challenge I ran into was trying to figure out a prompt for Gemini in order to produce a result that was not only accurate but also simple and easy to read. Too much information would be a problem, especially for younger users who are not familiar with specific terminology.

## Accomplishments that we're proud of
I'm proud of creating an app that can help empower teenage girls just like me and my friends to make healthy food choices that can help them even later in their lives. 

## What we learned
While making this project I learned a lot about implementing AI into code and our everyday lives. AI can sound like a confusing and overwhelming thing, but it's surprisingly easy to use.

## What's next for HealthyHer
Next, I'm thinking of making HealthyHer into a mobile app to reach a wider audience. I would also like to implement a social aspect into it, where users would be able to share their healthy food choices with other users. 


# How to run HealthyHer

HealthyHer is a web application that analyzes uploaded images of food items to provide detailed nutritional information, including calorie estimates and health assessments using AI.

## Features
- Upload an image of food.
- Receive details on the food items, their calories, and whether they are healthy or not.
- AI-generated responses powered by Google's Gemini API.

## Requirements
To run this project locally, you'll need the following:

- Python 3.7+
- Pip (Python package manager)
- Git
- A valid API key for Google's Gemini API
- Virtual environment (optional but recommended)

## Installation Instructions

### 1. Clone the Repository
First, clone this repository to your local machine:

```git clone https://github.com/unaysahr/HealthyHer.git
cd HealthyHer```

### 2. Set Up a Virtual Environment (optional but recommended)
Create and activate a virtual environment to keep your dependencies isolated:
```python -m venv venv
source venv/bin/activate  # On macOS/Linux```
# On Windows, use `venv\Scripts\activate`

### 3. Install Dependencies
Install the required dependencies listed in the requirements.txt file:
```pip install -r requirements.txt```

### 4. Configure Environment Variables
You'll need to create a .env file in the root of the project directory to store your Google Gemini API key and any other sensitive information. The format of the .env file should look like this:
```GOOGLE_API_KEY=your-google-gemini-api-key-here```
Make sure you have a valid API key from Google.

### 5. Running the Application
After setting up your environment, run the application using Streamlit:
```streamlit run app.py```

The application will be available at http://localhost:8501.

### 6. Uploading an Image and Testing
Navigate to the app in your browser.
Upload a food image by clicking the "Choose an image" button.
Click "Is it Healthy or Not" to get the AI-generated nutritional information.

Additional Notes
Make sure your Google Gemini API key is valid and has sufficient quota.
This project is designed for educational purposes.
Troubleshooting
If you encounter issues:

Ensure that all dependencies are correctly installed.
Verify that your API key is correct and that you're not exceeding any usage limits.


