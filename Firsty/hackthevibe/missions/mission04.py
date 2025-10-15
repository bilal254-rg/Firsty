import base64, time, sys

def run(username, xp, save_progress, caesar_decrypt):
    """
    Mission 04: Cipher Chain — Base64 + Caesar(3)
    - Secret is Base64 of a Caesar-shifted message.
    - Player must decode Base64, then decrypt Caesar (shift 3 back).
    """
    print("\nMission 04: Cipher Chain — Decode the Phantom Signal")
    print("A mysterious Base64 string was intercepted. Decode it, then reverse a Caesar(+3) shift.")
    print("\nRules: Type the final decrypted English phrase. Use 'hint' for a nudge, or 'reveal' to give up (no XP).")
    # This is the encoded payload (safe, short)
    # Original plaintext: "The phantom speaks"
    # Caesar +3 -> "Wkh skdwrp vshdfnv"
    # Base64 of that -> "V2toIHNrZHdycCB2c2hkZWZz" (we will compute below for honesty)
    # To avoid confusion, we will compute here properly so string matches.
    plaintext_caesar = "Wkh skdwrp vshdfnv"
    encoded = base64.b64encode(plaintext_caesar.encode()).decode()

    # For a little variety, print a masked sample and length
    print(f"\nIntercepted signal (Base64), length {len(encoded)} characters:")
    print(f"  > {encoded[:10]}...{encoded[-6:]}")
    attempts = 0
    start = time.time()

    while True:
        attempts += 1
        ans = input("\nEnter the final decrypted message (or 'hint'/'reveal'): ").strip()
        if not ans:
            print("Type something (or 'hint'/'reveal').")
            continue
        if ans.lower() == "hint":
            print("Hint: First decode Base64, then shift letters 3 positions back (Caesar -3).")
            continue
        if ans.lower() == "reveal":
            # show the two-step reveal
            decoded = base64.b64decode(encoded.encode()).decode()
            print(f"\nBase64 -> {decoded}")
            print(f"Caesar(-3) reveal -> {caesar_decrypt(decoded, 3)}")
            print("Mission aborted — no XP gained.")
            return xp

        # Check user's answer by reproducing correct transformation
        try:
            decoded = base64.b64decode(encoded.encode()).decode()
        except Exception:
            print("Internal decode error (weird). Ask Nova for help.")
            return xp

        final = caesar_decrypt(decoded, 3)
        # normalize for comparison
        if ans.lower().replace(" ", "") == final.lower().replace(" ", ""):
            elapsed = time.time() - start
            print("\n✅ Correct. Phantom signal decrypted.")
            print("+150 XP")
            xp += 150
            save_progress(username, xp)
            print(f"Total XP: {xp}   (Attempts: {attempts}, Time: {int(elapsed)}s)")
            print('New intel unlocked: "Phantom fragment: 0xF1A2"')
            return xp
        else:
            print("❌ Not right. Try again or type 'hint' for guidance.")
            if attempts >= 6:
                print("Tip: decode Base64 first and print the result to see the Caesar text.")
            continue
