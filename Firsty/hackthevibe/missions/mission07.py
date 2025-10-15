#!/usr/bin/env python3
# Mission 07 — Password Cracker (Layered Ciphers) — safe simulated puzzle

import time, base64, random, sys

def slow(t=0.25):
    time.sleep(t)

def xor_bytes(s: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(s)])

def caesar_decrypt_str(s: str, shift: int) -> str:
    out = []
    for ch in s:
        if 'a' <= ch <= 'z':
            out.append(chr((ord(ch) - 97 - shift) % 26 + 97))
        elif 'A' <= ch <= 'Z':
            out.append(chr((ord(ch) - 65 - shift) % 26 + 65))
        else:
            out.append(ch)
    return ''.join(out)

def run(username, xp, save_progress, caesar_decrypt):
    """
    Password Cracker — layered puzzle:
      plaintext -> Caesar(+3) -> XOR with short key -> Base64
    Player must reverse the three steps to find plaintext password.
    """
    # Keep a few plausible passwords and pick one for replayability
    candidates = ["silentkey", "shadowfox", "phantom1", "codeiskey", "n0vaagent"]
    plaintext = random.choice(candidates)

    # Transform: Caesar(+3), then XOR with short key, then base64 encode
    caesar_text = ''.join(
        chr((ord(c) - 97 + 3) % 26 + 97) if 'a' <= c <= 'z' else
        chr((ord(c) - 65 + 3) % 26 + 65) if 'A' <= c <= 'Z' else c
        for c in plaintext
    )

    xor_key = random.choice(["NOVA","KEY","X0R","salt"])
    xored = xor_bytes(caesar_text.encode(), xor_key.encode())
    encoded = base64.b64encode(xored).decode()

    attempts = 0
    hints_used = 0
    start = time.time()

    print("\nMission 07: Password Cracker — Layered Ciphers")
    print("A password was encrypted and intercepted. Reverse the layers to recover it.")
    print("Rules:")
    print(" - You may attempt guesses up to 8 times.")
    print(" - Type 'hint' for a nudge (costs 1 attempt).")
    print(" - Type 'simulate' to show one decoding step (costs 2 attempts).")
    print(" - Type 'reveal' to reveal the password (no XP).")
    slow(0.3)

    print(f"\nIntercepted payload (Base64), length {len(encoded)} characters:")
    print("  >", encoded)
    slow(0.2)

    while True:
        attempts += 1
        left = 9 - attempts  # attempts allowed: 8 (so after increment, 9-attempts is remaining)
        if left < 0:
            print("\nNo attempts left. Mission failed.")
            return xp

        ans = input(f"\nEnter password (Attempts left: {left}) or 'hint'/'simulate'/'reveal': ").strip()
        if not ans:
            print("Type something — a guess or 'hint'/'simulate'/'reveal'.")
            continue

        if ans.lower() == "hint":
            hints_used += 1
            attempts += 0  # hint counts as attempt cost is handled by attempts left calculation
            # choose a hint based on how many hints used
            if hints_used == 1:
                print("Hint 1: It's English, lowercase-ish, no spaces.")
            elif hints_used == 2:
                print("Hint 2: The Caesar shift used is small and positive.")
            else:
                print(f"Hint 3: The XOR key is a short uppercase word (length 3-4).")
            continue

        if ans.lower() == "simulate":
            # show intermediate layer (but cost 2 attempts)
            attempts += 1
            try:
                intermediate = base64.b64decode(encoded.encode())
                print("\nSimulate step -> Base64 decode (bytes shown):")
                print("  ", intermediate)
                print("Use XOR key to get Caesar text; then reverse Caesar.")
            except Exception as e:
                print("Simulation failed (weird).")
            continue

        if ans.lower() == "reveal":
            # show full reveal (no XP)
            print("\nReveal -> showing full decoding steps (no XP):")
            print("Base64 -> bytes:", base64.b64decode(encoded.encode()))
            print("XOR key (hidden during mission):", xor_key)
            print("Caesar(+3) text ->", caesar_text)
            print("Plaintext ->", plaintext)
            print("\nMission aborted — no XP gained.")
            return xp

        # check guess
        if ans == plaintext:
            elapsed = time.time() - start
            print("\n✅ Correct. Password recovered.")
            # XP calculation: base 200, minus a small penalty for hints or simulate,
            # plus speed bonus if quick (<45s)
            reward = 200
            reward -= 20 * (hints_used)            # each hint reduces reward
            if attempts <= 3:
                reward += 50  # speed bonus small
            if reward < 50:
                reward = 50
            print(f"+{reward} XP")
            xp += reward
            save_progress(username, xp)
            print(f"Total XP: {xp} (Attempts: {attempts}, Time: {int(elapsed)}s)")
            return xp
        else:
            print("❌ Not correct. Keep trying or use 'hint'/'simulate'/'reveal'.")
            if attempts >= 8:
                print("\nOut of attempts. Mission failed.")
                return xp
            continue
