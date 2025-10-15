import time, re, sys, random

def run(username, xp, save_progress, caesar_decrypt):
    """
    Mission 05 — Log-Forensics (Find the Intruder)
    - Parse the fake server log and find the malicious IP & username.
    - Then choose an action to execute (simulated).
    """
    log = r'''
2025-10-15T07:21:03Z 10.0.0.12 user=alice action=login status=success src=203.0.113.17
2025-10-15T07:21:11Z 10.0.0.12 user=bob action=read status=ok src=198.51.100.5
2025-10-15T07:22:03Z 10.0.0.12 user=mallory action=login status=fail src=198.51.100.42
2025-10-15T07:22:07Z 10.0.0.12 user=mallory action=login status=fail src=198.51.100.42
2025-10-15T07:22:13Z 10.0.0.12 user=mallory action=login status=success src=198.51.100.42
2025-10-15T07:22:18Z 10.0.0.12 user=mallory action=read status=ok src=198.51.100.42 file=/srv/secret/alpha.txt
2025-10-15T07:23:00Z 10.0.0.12 user=carol action=login status=success src=203.0.113.21
2025-10-15T07:23:10Z 10.0.0.12 user=mallory action=download status=ok src=198.51.100.42 file=/srv/secret/alpha.txt size=13B
2025-10-15T07:23:20Z 10.0.0.12 user=alice action=logout status=ok src=203.0.113.17
2025-10-15T07:24:55Z 10.0.0.12 user=bob action=write status=ok src=198.51.100.5 file=/var/log/app.log
2025-10-15T07:25:02Z 10.0.0.12 user=mallory action=logout status=ok src=198.51.100.42
2025-10-15T07:26:13Z 10.0.0.12 user=eviluser action=login status=fail src=192.0.2.77
2025-10-15T07:26:20Z 10.0.0.12 user=eviluser action=login status=fail src=192.0.2.77
2025-10-15T07:26:25Z 10.0.0.12 user=eviluser action=login status=fail src=192.0.2.77
2025-10-15T07:26:31Z 10.0.0.12 user=eviluser action=login status=success src=192.0.2.77
2025-10-15T07:26:35Z 10.0.0.12 user=eviluser action=read status=ok src=192.0.2.77 file=/srv/secret/beta.txt
2025-10-15T07:26:50Z 10.0.0.12 user=eviluser action=download status=ok src=192.0.2.77 file=/srv/secret/beta.txt size=21B
2025-10-15T07:27:00Z 10.0.0.12 user=eviluser action=logout status=ok src=192.0.2.77
'''
    print("\nMission 05: Log-Forensics — Find the Intruder")
    print("We intercepted a short server log. Your job: identify the malicious IP and username that exfiltrated secret data.")
    print("Rules: Inspect the log, find the suspicious actor (IP + username). Then choose an action: 'block', 'revoke', or 'exfil'.")
    print("Tip: look for sequences of failed logins followed by success, file downloads, or unusual file access.\n")
    print("---- LOG START ----")
    print(log)
    print("---- LOG END ----\n")

    malicious_ip = None
    malicious_user = None

    # Simple heuristic: IPs with multiple failed then success and a download
    # scan for lines and look for repeated src and download actions
    lines = [l.strip() for l in log.strip().splitlines() if l.strip()]
    counts = {}
    downloads = {}
    for ln in lines:
        m = re.search(r'src=([0-9.]+)', ln)
        u = re.search(r'user=([^\s]+)', ln)
        act = re.search(r'action=([^\s]+)', ln)
        if m:
            ip = m.group(1)
            counts.setdefault(ip, 0)
            counts[ip] += 1
            if act and act.group(1) in ('download','read'):
                downloads.setdefault(ip, []).append(ln)
        if u:
            user = u.group(1)
    # decide malicious candidate: IP with download and repeated attempts
    candidates = [ip for ip, d in downloads.items() if len(d) >= 1]
    if candidates:
        # prefer the IP that appears most often among candidates
        malicious_ip = sorted(candidates, key=lambda i: counts.get(i,0), reverse=True)[0]
        # now get username tied to this IP by scanning lines
        for ln in lines:
            if malicious_ip in ln:
                mu = re.search(r'user=([^\s]+)', ln)
                if mu:
                    malicious_user = mu.group(1)
                    break

    attempts = 0
    while True:
        attempts += 1
        ans = input("\nEnter 'ip username' (e.g. 198.51.100.42 mallory) or type 'hint'/'reveal': ").strip()
        if not ans:
            print("Type something (or 'hint'/'reveal').")
            continue
        if ans.lower() == 'hint':
            print("Hint: Look for repeated failed logins followed by success, and file download entries. Check src= fields.")
            continue
        if ans.lower() == 'reveal':
            print(f"\nReveal -> IP: {malicious_ip}   user: {malicious_user}")
            print("Mission aborted — no XP gained.")
            return xp

        parts = ans.split()
        if len(parts) != 2:
            print("Reply with two tokens: ip username")
            continue

        ip_guess, user_guess = parts[0].strip(), parts[1].strip()
        if ip_guess == malicious_ip and user_guess == malicious_user:
            print("\n✅ Correct. Intruder identified.")
            # next stage: choose action
            print("\nChoose an action to execute (simulated):")
            print("  1. block   -> simulate firewall block (no real network commands)")
            print("  2. revoke  -> simulate revoking user credentials")
            print("  3. exfil   -> extract the stolen file/flag (mission goal)")
            action = input("Action (block/revoke/exfil): ").strip().lower()
            if action == 'block':
                print(f"\nSimulating firewall rule: block {malicious_ip}")
                print("Firewall rule applied (simulated). +80 XP")
                xp += 80
                save_progress(username, xp)
                return xp
            elif action == 'revoke':
                print(f"\nSimulating credential revocation for user: {malicious_user}")
                print("Credentials revoked (simulated). +80 XP")
                xp += 80
                save_progress(username, xp)
                return xp
            elif action == 'exfil':
                # extract the small flag hidden in file content (simulate)
                flag = "FLAG{log_forensics_mastery_05}"
                print("\nSimulating file recovery from /srv/secret/beta.txt ...")
                time.sleep(1.0)
                print(f"Recovered file contents: \"{flag}\"")
                print("+160 XP")
                xp += 160
                save_progress(username, xp)
                return xp
            else:
                print("Unknown action. Try again.")
                continue
        else:
            print("❌ Not the intruder. Keep digging or type 'hint'.")
            if attempts >= 6:
                print("Tip: look for download actions and the src= IP associated with them.")
            continue
