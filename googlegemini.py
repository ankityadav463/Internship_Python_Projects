import google.generativeai as genai
key = "AIzaSyBQbiWPC2FHZbX1IdhzJCwK-p3r_1993MQ"
print(key)
genai.configure(api_key=key)
Model = genai.GenerativeModel("gemini-2.5-flash")
while True:
    user = input("What do you want To Search,\n  Type 'exit' to close: ")

    if user.lower() == "exit":
        print("bye bye")
        break

    response = Model.generate_content(user)
    print("bot:", response.text)