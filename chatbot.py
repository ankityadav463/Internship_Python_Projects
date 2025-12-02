print("Radhe Radhe...\n")
import google.generativeai as genai

key = "AIzaSyDT-JmUVtd-l1869o5wXErYR8bRchu8otE"
print(key)
genai.configure(api_key=key)
Model = genai.GenerativeModel("gemini-2.5-pro")
while True:
    user = input("What do you want To Search  Type 'exit' to close: ")

    if user.lower() == "exit":
        print("bye bye")
        break

    response = Model.generate_content(user)
    print("bot:", response.text)