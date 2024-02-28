def main():
    numbers = []


    while True:
        user_input = input("Syötä luku (tyhjä rivi lopettaa): ")
        if user_input == '':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Virheellinen syöte! Syötä luku tai jätä tyhjä rivi lopettaaksesi.")

    if numbers:
        min_number = min(numbers)
        max_number = max(numbers)
        print("Pienin luku:", min_number)
        print("Suurin luku:", max_number)
    else:
        print("Et syöttänyt yhtään lukua.")







