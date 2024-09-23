# import os to obtain Anthropic API KEY
import os

# import anthropic to create instance of 'Claude'
import anthropic

# creating an instance of 'Claude' - that we can interact with and send messages to
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

# setup message with neccecary fields (important things are the role and the content)
message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)

# print the content of the message, which should be Claude's response
print(message.content)
