def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)


texts = [
    "Halo, apa kabar?",
    "Jangan lupa makan siang.",
    "Sampai ketemu besok!",
]
sent_messages = []

send_messages(texts[:], sent_messages)

print("\nIsi list texts (asli):")
print(texts)

print("\nIsi list sent_messages:")
print(sent_messages)