# WhatsappGTP

![alt text](/logo.jpeg?raw=true)


## Introduction

This project is a simple chatbot for WhatsApp using OpenAI's GPT-3 language model, ChatGPT. The chatbot uses Twilio's API to communicate with WhatsApp. The configuration of the bot is done through a file called keys.json where you will need to input your OpenAI API key and Twilio API keys.

## Why use this chatbot?

ChatGPT is one of the most advanced language models developed by OpenAI and has been trained on a massive corpus of data. This allows the chatbot to generate human-like responses and handle a wide range of topics with accuracy and efficiency. Additionally, Twilio's API makes it easy to integrate the chatbot with WhatsApp, allowing you to offer customer support or handle other tasks directly through the messaging platform. Overall, this chatbot offers a convenient and effective solution for businesses and organizations looking to improve their communication and customer service.

## Configuration

To install and use the program, follow these steps:

1. Clone the repository to your local machine.
2. Obtain your OpenAI API key from the OpenAI website and your Twilio    API keys from the Twilio website.
3. Input your API keys into the keys.json file in the following format:

```
{
  "openai": "your_openai_key",
   "twilio_account_sid": "your_twilio_account_sid",
   "twilio_auth_token": "your_twilio_auth_token",
   "whatsapp_number": "your_twilio_whatsapp_number"
}
```

### OpenAI API Key
1. Create a free account on the OpenAI website https://beta.openai.com/signup/.
2. After you have signed up and logged in, navigate to the API keys section of the OpenAI website.
3. Generate a new API key and copy it to your clipboard.
### Twilio API Key
1. Create a free account on the Twilio website https://www.twilio.com/try-twilio.
2. After you have signed up and logged in, navigate to the Console.
In the Console, generate a new API key by following the steps provided by Twilio.
3. Copy the API key to your clipboard.
4. Once you have obtained both API keys, you can add them to the keys.json file, as described in the "Configuration" section.

### Setting up a Tunnel with ngrok

In order to use the chatbot with the Twilio API, it is necessary to create a secure tunnel to your local Flask app using ngrok. This will allow you to receive incoming messages from Twilio through the publicly accessible ngrok URL.

1. Download and install ngrok by following the instructions on their website.
2. Start a new ngrok tunnel by running ngrok http 5000 in your terminal.
3. You should see a URL similar to https://<your_ngrok_subdomain>.ngrok.io displayed in the terminal.
4. Use this URL as the webhook for your Twilio WhatsApp number in the Twilio Console.

Note: The ngrok URL will change every time you restart the ngrok tunnel, so make sure to update the webhook in the Twilio Console accordingly.

## Use 

Using the chatbot is simple. Just start a conversation with the Twilio WhatsApp number associated with the chatbot and start chatting! The chatbot will respond to your messages in real-time, providing you with answers and information on a wide range of topics.

Here are a few examples of what you can ask the chatbot:
Just chat with it. Send a message starting with "image:" to generate a photo. For example: 

- "What is GPT-3?"
- "Who is the author of The Great Gatsby?"
- "What is the meaning of life?"
- "What is the capital of Spain?"

Additionally, the chatbot is capable of generating images based on a given description. To generate an image, simply send a message in the following format: "image: [your description]". 

For example, you could send the message "image: An apple is running under the eiffel tower" and the chatbot will generate an image based on the description provided.

![alt text](/eiffel.jpeg?raw=true)


## Docker installation

In addition to using the docker-compose.yml file, you will also need to build the Docker image before you can run the app in a container. Here's how:

1. Open a terminal window and navigate to the directory containing the Dockerfile.
2. Run the following command to build the Docker image: 

> docker build -t whatsapp-gpt .

## Conclusion

You should be able to get started with using the chatbot. If you have any questions or run into any issues, feel free to reach out to the project's maintainers for support.

