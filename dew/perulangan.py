def main(name):
    output = ""
    for i in range(1, 101):
        if i % 10 == 0:
            output += f"{name}\n" * 3  # Mengulang nama "Dewi" sebanyak 3 kali
        else:
            output += str(i) + "\n"
    return output

print(main("Dewi Margiani"))