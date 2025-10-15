import time, random, sys

def slow(t=0.35):
    time.sleep(t)

def run(username, xp, save_progress, caesar_decrypt):
    """
    Mission 07 — Port Sweep (Simulated)
    - Simulated host with ports/services. Find the open ports and choose an action.
    """
    print("\nMission 07: Port Sweep — Scan & Map the Network")
    print("You have access to a simulated network console. Identify open ports on the target and act.")
    print("Commands: type ports separated by commas (e.g. 22,80,443), or 'hint', or 'reveal' (no XP).")
    print("Actions after identification: 'secure' (patch/close), 'probe' (gather more intel), 'ignore'.\n")

    # Simulated target (randomized per run for replayability)
    hosts = {
        "alpha.srv": {22:"ssh", 80:"http", 443:"https", 8080:"http-alt", 3306:"mysql", 6379:"redis"},
        "beta.srv":  {21:"ftp", 22:"ssh", 25:"smtp", 110:"pop3", 143:"imap", 5000:"serviceX"},
        "gamma.srv": {53:"dns", 161:"snmp", 69:"tftp", 8000:"webapp", 9000:"custom"},
    }
    target = random.choice(list(hosts.keys()))
    # pick a subset of ports to be "open"
    candidate_ports = list(hosts[target].keys())
    open_count = random.choice([2,3,3])  # 2 or 3 open ports
    open_ports = sorted(random.sample(candidate_ports, open_count))

    # To make it feel realistic, create noisy banner lines
    print(f"Target: {target}")
    print("Starting lightweight SYN-style sweep (simulated)...")
    slow(0.6)
    print("\nNetwork console output (simulated):")
    # show hints/noise — not explicit open list, just banners and latency clues
    for p in sorted(candidate_ports):
        latency = random.randint(1,120)
        banner_chance = random.random()
        banner = ""
        if p in open_ports and banner_chance > 0.4:
            banner = f" - banner: {hosts[target][p]}/1.0"
        elif banner_chance > 0.95:
            banner = " - banner: UNKNOWN_SERVICE"
        print(f"probe -> port {p} ... rtt {latency}ms{banner}")
        slow(0.05)

    attempts = 0
    while True:
        attempts += 1
        ans = input("\nEnter suspected open ports (comma-separated), or 'hint'/'reveal': ").strip()
        if not ans:
            print("Type something — or 'hint'/'reveal'.")
            continue
        if ans.lower() == "hint":
            print("Hint: look for lower RTTs and visible banners mentioning service names.")
            continue
        if ans.lower() == "reveal":
            print(f"\nReveal -> open ports: {', '.join(str(p) for p in open_ports)}  (services: {', '.join(hosts[target][p] for p in open_ports)})")
            print("Mission aborted — no XP gained.")
            return xp

        # parse guess
        parts = [p.strip() for p in ans.replace(" ", "").split(",") if p.strip().isdigit()]
        try:
            guessed = sorted(int(p) for p in parts)
        except:
            print("Please enter numeric port numbers separated by commas.")
            continue

        # check correctness (exact match)
        if guessed == open_ports:
            print("\n✅ Correct ports identified.")
            # action stage
            print("\nChoose an action to execute:")
            print("  secure -> simulate patch/close ports (recommended)")
            print("  probe  -> simulate deeper probe for extra intel (less safe)")
            print("  ignore -> leave as-is (no further action)")
            action = input("Action (secure/probe/ignore): ").strip().lower()
            if action == "secure":
                # simulate action with dramatic output
                print(f"\nSimulating secure action on {target}:")
                slow(0.4)
                for p in open_ports:
                    print(f"  applying rule: deny {p}/tcp ... ok")
                    slow(0.25)
                print("\nTarget hardened (simulated). +120 XP")
                xp += 120
                # small bonus for securing vs probing
                print("+30 XP security bonus")
                xp += 30
                save_progress(username, xp)
                return xp
            elif action == "probe":
                print("\nSimulating deeper probe (simulated): gathering service versions...")
 



python3 ~/Firsty/hackthevibe/hackthevibe.pypython3 ~/Firsty/hackthevibe/hackthevibe.py

cd ~/Firsty/hackthevibe/missions
python3 ~/Firsty/hackthevibe/hackthevibe.py
cd ~/Firsty/hackthevibe/missions

cat > mission07.py <<'PY'
import time, random, sys

def slow(t=0.35):
    time.sleep(t)

def run(username, xp, save_progress, caesar_decrypt):
    """
    Mission 07 — Port Sweep (Simulated)
    - Simulated host with ports/services. Find the open ports and choose an action.
    """
    print("\nMission 07: Port Sweep — Scan & Map the Network")
    print("You have access to a simulated network console. Identify open ports on the target and act.")
    print("Commands: type ports separated by commas (e.g. 22,80,443), or 'hint', or 'reveal' (no XP).")
    print("Actions after identification: 'secure' (patch/close), 'probe' (gather more intel), 'ignore'.\n")

    # Simulated target (randomized per run for replayability)
    hosts = {
        "alpha.srv": {22:"ssh", 80:"http", 443:"https", 8080:"http-alt", 3306:"mysql", 6379:"redis"},
        "beta.srv":  {21:"ftp", 22:"ssh", 25:"smtp", 110:"pop3", 143:"imap", 5000:"serviceX"},
        "gamma.srv": {53:"dns", 161:"snmp", 69:"tftp", 8000:"webapp", 9000:"custom"},
    }
    target = random.choice(list(hosts.keys()))
    # pick a subset of ports to be "open"
    candidate_ports = list(hosts[target].keys())
    open_count = random.choice([2,3,3])  # 2 or 3 open ports
    open_ports = sorted(random.sample(candidate_ports, open_count))

    # To make it feel realistic, create noisy banner lines
    print(f"Target: {target}")
    print("Starting lightweight SYN-style sweep (simulated)...")
    slow(0.6)
    print("\nNetwork console output (simulated):")
    # show hints/noise — not explicit open list, just banners and latency clues
    for p in sorted(candidate_ports):
        latency = random.randint(1,120)
        banner_chance = random.random()
        banner = ""
        if p in open_ports and banner_chance > 0.4:
            banner = f" - banner: {hosts[target][p]}/1.0"
        elif banner_chance > 0.95:
            banner = " - banner: UNKNOWN_SERVICE"
        print(f"probe -> port {p} ... rtt {latency}ms{banner}")
        slow(0.05)

    attempts = 0
    while True:
        attempts += 1
        ans = input("\nEnter suspected open ports (comma-separated), or 'hint'/'reveal': ").strip()
        if not ans:
            print("Type something — or 'hint'/'reveal'.")
            continue
        if ans.lower() == "hint":
            print("Hint: look for lower RTTs and visible banners mentioning service names.")
            continue
        if ans.lower() == "reveal":
            print(f"\nReveal -> open ports: {', '.join(str(p) for p in open_ports)}  (services: {', '.join(hosts[target][p] for p in open_ports)})")
            print("Mission aborted — no XP gained.")
            return xp

        # parse guess
        parts = [p.strip() for p in ans.replace(" ", "").split(",") if p.strip().isdigit()]
        try:
            guessed = sorted(int(p) for p in parts)
        except:
            print("Please enter numeric port numbers separated by commas.")
            continue

        # check correctness (exact match)
        if guessed == open_ports:
            print("\n✅ Correct ports identified.")
            # action stage
            print("\nChoose an action to execute:")
            print("  secure -> simulate patch/close ports (recommended)")
            print("  probe  -> simulate deeper probe for extra intel (less safe)")
            print("  ignore -> leave as-is (no further action)")
            action = input("Action (secure/probe/ignore): ").strip().lower()
            if action == "secure":
                # simulate action with dramatic output
                print(f"\nSimulating secure action on {target}:")
                slow(0.4)
                for p in open_ports:
                    print(f"  applying rule: deny {p}/tcp ... ok")
                    slow(0.25)
                print("\nTarget hardened (simulated). +120 XP")
                xp += 120
                # small bonus for securing vs probing
                print("+30 XP security bonus")
                xp += 30
                save_progress(username, xp)
                return xp
            elif action == "probe":
                print("\nSimulating deeper probe (simulated): gathering service versions...")
                slow(0.6)
                for p in open_ports:
                    v = hosts[target][p]
                    ver = f"v{random.randint(1,3)}.{random.randint(0,9)}"
                    print(f"  {p}/tcp -> {v} ({ver}) fingerprint ok")
                    slow(0.2)
                print("\nYou gathered intel. +120 XP")
                xp += 120
                save_progress(username, xp)
                return xp
            elif action == "ignore":
                print("\nNo action taken. Target unchanged. +60 XP (for identification only).")
                xp += 60
                save_progress(username, xp)
                return xp
            else:
                print("Unknown action. Try again.")
                continue
        else:
            print("❌ Not quite. That's not the set of open ports. Try again or type 'hint'.")
            if attempts >= 6:
                print("Tip: compare reported RTTs — lower values and banners often indicate open ports.")
            continue
