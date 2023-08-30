FROM ubuntu:latest

# Create app directory
WORKDIR /app

# Fix me!!
ENV STT_REGION="japaneast"
ENV STT_RESOURCE_ID="/subscriptions/3ab8a6b6-76b6-41bd-be28-699f18363862/resourceGroups/aoai_refer_art_rg/providers/Microsoft.CognitiveServices/accounts/demo-speech-service-13579"
ENV TEXT_ANALYTICS_ENDPOINT="https://demo-language-service-13579.cognitiveservices.azure.com"
ENV AOAI_ENDPOINT="https://demo-openai-service-13579.openai.azure.com"
ENV AOAI_MODEL="gpt-4-deployment"

RUN apt update
RUN apt install python3 python3-pip curl -y

RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Install app dependencies
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Bundle app source
COPY . .

EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
