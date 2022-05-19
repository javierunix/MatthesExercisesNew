# Function that prints all messages from list.
def send_messages(incoming_messages, sent_messages):
    """
    Simulate sending each messages, until none are left.
    Move each message to sent_messages after printing.
    """
    while incoming_messages:
        current_message = incoming_messages.pop()
        print(f"Sending message: '{current_message}'.")
        sent_messages.append(current_message)


def show_sent_messages(sent_messages):
    """Show all messages that were sent."""
    print("\nThe following messages have been sent.")
    for sent_message in sent_messages:
        print(sent_message)


incoming_messages = ['Hello, worlsd!', 'How are you?', 'Please to meet you.']
sent_messages = []


# To avoid original list modification, pass a copy of the list,
#   passing incoming_messages[:] as argument.
send_messages(incoming_messages[:], sent_messages)
show_sent_messages(sent_messages)

print("\nChecking the lists content:")
print("\nOriginal list:")
print(incoming_messages)
print("\nNew list:")
print(sent_messages)
