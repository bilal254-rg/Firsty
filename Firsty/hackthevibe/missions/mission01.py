def run(username, xp, save_progress, caesar_decrypt):
    print("\nMission 01: Crack the Cipher")
    enc = "Wkh frgh lv wkh nhb"
    print("Encrypted message:")
    print("  >", enc)
    print("\nTip: It's a Caesar cipher. Try simple shifts (0-25).")
    attempts = 0
    while True:
        attempts += 1
        ans = input("\nEnter the decrypted message: ").strip()
        if ans.lower().replace(" ", "") == caesar_decrypt(enc, 3).lower().replace(" ", ""):
            print("\n✅ Correct. Access granted. +50 XP")
            print("New intel unlocked: \"In silence, you find clarity.\"")
            xp += 50
            save_progress(username, xp)
            print(f"Total XP: {xp}")
            break
        else:
            print("❌ Nope. Keep trying or type 'hint' for help.")
            if ans.lower() == "hint":
                print("Hint: Try decoding by shifting letters 3 positions backwards.")
            if attempts >= 6:
                print("Need a push? Type 'reveal' to reveal the answer (kills XP).")
            if ans.lower() == "reveal":
                print("\nRevealed answer: ", caesar_decrypt(enc, 3))
                break
    return xp
