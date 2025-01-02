import random
with open("text.txt", "w") as file:
    file.write(''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()", k=1_000_000)))

def litery(file_1):
    slovnuk = {}
    with open(file_1, 'r') as file:
        for n in file:
            for m in n:
                if m.isalpha():
                    m = m.lower()
                    slovnuk[m] = slovnuk.get(m, 0) + 1
    return slovnuk
result = litery("text.txt")
print(result)


