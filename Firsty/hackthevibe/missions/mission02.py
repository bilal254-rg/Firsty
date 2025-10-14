def run(username, xp, save_progress, caesar_decrypt):
    print("\nMission 02: Logic Lockdown 🔐")
    print("You've reached the 'Pattern Terminal'.")
    print("To unlock it, find the next number in the sequence:\n")
    print("  2, 6, 12, 20, 30, ?")
    print("\nTip: Observe the pattern carefully 👀")

    correct = "42"
    attempts = 0
    while True:
        ans = input("\nEnter your answer: ").strip()
        attempts += 1
        if ans == correct:
            print("\n✅ Access granted. +70 XP")
            print("You cracked the logic lock, " + username + "!")
            xp += 70
            save_progress(username, xp)
            print(f"Total XP: {xp}")
            break
        elif ans.lower() == "hint":
            print("Hint: Think of how each number grows (n² + n).")
        elif ans.lower() == "reveal":
            print("Revealed answer: 42 (since 6×7)")
            break
        else:
            print("❌ Incorrect. Try again or type 'hint' for a clue.")
            if attempts >= 5:
                print("Still stuck? Type 'reveal' to see the answer.")
    return xp
