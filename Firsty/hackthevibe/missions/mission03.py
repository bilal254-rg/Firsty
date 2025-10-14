import time, random, sys, os

def _slow(msg, t=0.05):
    for ch in msg:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(t)
    print()

def run(username, xp, save_progress, caesar_decrypt):
    print("\nMission 03: Vault Break — Simulated Brute-Force (file-based)")
    print("This is a safe simulation (puzzle).")

    pw_file = os.path.join(os.path.dirname(__file__), "passwords.txt")
    if os.path.exists(pw_file):
        with open(pw_file, "r") as f:
            options = [line.strip() for line in f if line.strip()]
    else:
        options = ["omega7","echo9","silent1","night5"]

    # Guard: ensure options isn't empty
    if not options:
        print("No candidate passwords found in passwords.txt. Ask Nova to help fix it.")
        return xp

    secret = random.choice(options)
    print(f"\nVault: password length = {len(secret)} characters; contains letters + digits.")
    masked = "*" * len(secret)
    attempts_left = 8
    hint_used = False

    while attempts_left > 0:
        print(f"\nVault input: {masked}   Attempts left: {attempts_left}")
        guess = input("Enter password (or type 'hint'/'simulate'/'reveal'): ").strip()

        if not guess:
            print("Type something — or use 'hint'/'simulate'/'reveal'.")
            continue
        if guess.lower() == "hint":
            if attempts_left <= 1:
                print("No attempts left to use a hint.")
                continue
            attempts_left -= 1
            hint_used = True
            hint_type = random.choice(["first_char","pattern"])
            if hint_type == "first_char":
                print(f"Hint: first character is '{secret[0]}'")
            else:
                print("Hint: pattern looks like a short word followed by a single digit.")
            continue
        if guess.lower() == "simulate":
            _slow("\nSimulating harmless brute-force (demo)...", 0.03)
            bar_len = 30
            for i in range(bar_len+1):
                pct = int(i/bar_len*100)
                sys.stdout.write(f"\r[{'='*i}{' '*(bar_len-i)}] {pct}%")
                sys.stdout.flush()
                time.sleep(0.03)
            print("\nSimulation complete. (Visual only.)")
            continue
        if guess.lower() == "reveal":
            print(f"\nRevealed (no XP): {secret}")
            print("Mission aborted — no XP gained.")
            return xp

        attempts_left -= 1
        if guess == secret:
            reward = 100 if not hint_used else 60
            print("\n✅ Vault opened. Access granted.")
            print(f"+{reward} XP")
            xp += reward
            save_progress(username, xp)
            print(f"Total XP: {xp}")
            return xp
        else:
            correct_pos = sum(1 for a,b in zip(guess, secret) if a==b)
            print(f"❌ Incorrect. Characters correct in correct position: {correct_pos}")
            if attempts_left == 0:
                print("\nNo attempts left. Vault locked. No XP for this run.")
                return xp
            else:
                continue
    return xp
