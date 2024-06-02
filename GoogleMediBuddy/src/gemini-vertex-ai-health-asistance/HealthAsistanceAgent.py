from google.oauth2 import service_account
from dotenv import load_dotenv
import google.auth.transport.requests
import requests
import json
import os
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models


def main():
    # access_token = get_access_token()
    generate()


def get_access_token():
    # First Authenticate by downloading google json file and put into src location path
    # and also give googleapis cloud-plateform auth url
    credentials = service_account.Credentials.from_service_account_file(
        "google account Authenticate filename",
        scopes=["googleapis cloud-plateform auth url"]
    )
    credentials.refresh(google.auth.transport.requests.Request())
    return credentials.token


def vertex_ai_prompt():
    pass


def generate():
    vertexai.init(project="nodal-skein-424404-i2", location="asia-south1")
    model = GenerativeModel("gemini-1.5-flash-001", )
    response = model.generate_content(
        [
            """
            Act as a knowledgeable Health care assistant.
            A patient is in <Location> and does not wish to travel more than 40 miles. 
            The patient does not have health insurance.
            Provide five low-cost or no-cost options for obtaining necessary <type> lab services.
            The options should consider the patient\'s financial constraints, prioritize safety and quality of service.
            The options should include precise locations or contact information when possible.
    
            input: A patient\'s  Location
            output: New Delhi
            
            input: Type of lab services
            output: Urine test
            """
            , get_user_prompt()],
        generation_config=generation_config,
        safety_settings=safety_settings,
    )
    print(response.candidates[0].content.parts[0].text)
    pass


def get_user_prompt():
    print("Type a prompt.")

    # {input: {get_user_prompt()} output:}

    return input()


generation_config = {

    "max_output_tokens": 8192,

    "temperature": 1,

    "top_p": 0.95,

}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

# generate()

if __name__ == "__main__":
    main()