import openai

try:
  f = open(".api_key", "r")
  openai.api_key = f.read().split("\n")[0]
  f.close()
except:
  print("[ ERROR ] - Cannot read .api_key file for a valid token...")
  exit()

def ask_question(prompt):
  completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

  message = completions.choices[0].text
  return message

question = input("Enter your question: ")
answer = ask_question(question)
print(answer)
