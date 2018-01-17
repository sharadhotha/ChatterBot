import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("init.aiml")

# Press CTRL-C to break this loop
while True:
    print kernel.respond(raw_input("Enter your message >> "))