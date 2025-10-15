import base64, time, sys

def slow(t): time.sleep(t)

def caesar_shift(s, shift):
    out = []
    for ch in s:
        if 'a' <= ch <= 'z':
            out.append(chr((ord(ch)-97+shift) % 26 + 97))
        elif 'A' <= ch <= 'Z':
            out.append(chr((ord(ch)-65+shift) % 26 + 65))
        else:
            out.append(ch)
    return ''.join(out)

def vigenere_encrypt(plaintext, key):
    out = []
    ki = 0
    key = key.lower()
    for ch in plaintext:
        if ch.isalpha():
            base = 97 if ch.islower() else 65
            k = ord(key[ki % len(key)]) - 97
            out.append(chr((ord(ch) - base + k) % 26 + base))
            ki += 1
        else:
            out.append(ch)
    return ''.join(out)

def vigenere_decrypt(cipher, key):
    out = []
    ki = 0
    key = key.lower()
    for ch in cipher:
        if ch.isalpha():
            base = 97 if ch.islower() else 65
            k = ord(key[ki % len(key)]) - 97
            out.append(chr((ord(ch) - base - k) % 26 + base))
            ki += 1
        else:
            out.append(ch)
    return ''.join(out)

def run(username, xp, save_progress, caesar_decrypt):
    """
    Mission 06: Cipher Chain II
    Chain: plaintext -> Caesar(+3) -> Vigenere(key) -> Base64 (encoded)
    To solve: Base64 decode -> Vigenere-decrypt (same key) -> Caesar(-3)
    """
    print("\nMission 06: Cipher Chain II — Decode the Phantom Layer")
    print("We intercepted a layered payload. Decode Base64, undo Vigenère, then reverse Caesar(+3).")
    print("Commands: 'hint' (nudge), 'reveal' (show steps, no XP)\n")

    # --- mission parameters (computed here so encoded is consistent) ---
    plaintext = "Operation midnight complete"
    # step1: Caesar +3
    c1 = caesar_shift(plaintext, 3)
    # step2: Vigenere encrypt with key
    key = "NOVA"
    v = vigenere_encrypt(c1, key)
    # step3: Base64 encode
    encoded = base64.b64encode(v.encode()).decode()

    # display masked preview
    print(f"Intercepted payload (Base64), length {len(encoded)} characters:")
    print(f"  > {encoded[:12]}...{encoded[-8:]}")
    attempts = 0
    start = time.time()

    while True:
        attempts += 1
        ans = input("\nEnter final decrypted phrase (or 'hint'/'reveal'): ").strip()
        if not ans:
            print("Type something (or 'hint'/'reveal').")
            continue
        if ans.lower() == "hint":
            print("Hint: First Base64-decode. Then reverse Vigenère with key 'NOVA'. Finally shift letters 3 left.")
            continue
        if ans.lower() == "reveal":
            # show the actual steps (no XP)
            print("\n--- Reveal ---")
            print("Base64 ->", base64.b64decode(encoded).decode())
            print("Vigenere(-key=NOVA) ->", vigenere_decrypt(base64.b64decode(encoded).decode(), key))
            print("Caesar(-3) ->", caesar_decrypt(vigenere_decrypt(base64.b64decode(encoded).decode(), key), 3))
            print("Mission aborted — no XP gained.")
            return xp

        # compute correct final
        try:
            decoded_b64 = base64.b64decode(encoded).decode()
        except Exception:
            print("Internal decode error. Ask Nova for help.")
            return xp

        after_vig = vigenere_decrypt(decoded_b64, key)
        final = caesar_decrypt(after_vig, 3)

        if ans.lower().replace(" ", "") == final.lower().replace(" ", ""):
            elapsed = time.time() - start
            print("\n✅ Correct. Layer decoded.")
            print("+200 XP")
            xp += 200
            save_progress(username, xp)
            print(f"Total XP: {xp}   (Attempts: {attempts}, Time: {int(elapsed)}s)")
            print('New intel unlocked: "Phantom fragment: 0xC6B4"')
            return xp
        else:
            print("❌ Not right. Try again or type 'hint' for a nudge.")
            if attempts >= 6:
                print("Tip: decode Base64 first and inspect the Vigenère text for repeated patterns.")
            continue
