def brute_force_wordlist(wordlist, password):
    with open(wordlist, 'r') as file:
        for line in file:
            attempt = line.strip()
            if attempt == password:
                return f"Passwort gefunden: {attempt}"
    return "Passwort nicht in der Wordlist gefunden."

# Geben Sie den Dateipfad zur Wordlist und das zu knackende Passwort an
wordlist = "wordlist.txt"
password = "geheimespasswort"

result = brute_force_wordlist(wordlist, password)
print(result)
