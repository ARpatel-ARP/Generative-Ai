from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

# response = model.invoke("name the president of pakistan")
# response = model.invoke("Why pakistan does not face revolution")

# print(response.content)

from langchain_mistralai import ChatMistralAI
model = init_chat_model(model="mistral-small-latest", temperature=0.9, max_tokens=50)
responseM = model.invoke("write a joke on indian education system")
print(responseM.content)