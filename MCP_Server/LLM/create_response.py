def create_response(client, deployment_name, message):
    text_output = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ]

    response = client.chat.completions.create(
        model = deployment_name,
        messages = text_output
    )

    return response.choices[0].message.content