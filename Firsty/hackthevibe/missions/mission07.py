import time, random

def slow(t=0.35):
    time.sleep(t)

def run(username, xp, save_progress, caesar_decrypt):
    """
    Mission 07 — Port Sweep (Simulated)
    """
    print("\nMission 07: Port Sweep — Scan & Map the Network")
    
    hosts = {
        "alpha.srv": {22:"ssh", 80:"http", 443:"https", 8080:"http-alt"},
        "beta.srv": {21:"ftp", 22:"ssh", 25:"smtp", 110:"pop3"},
        "gamma.srv": {53:"dns", 161:"snmp", 69:"tftp"}
    }

    target = random.choice(list(hosts.keys()))
    candidate_ports = list(hosts[target].keys()) + random.sample(range(1024, 1050), 2)
    open_ports = sorted(random.sample(list(hosts[target].keys()), 2))

    print(f"Target: {target}")
    slow(0.5)

    print("\nNetwork console output (simulated):")
    for p in sorted(candidate_ports):
        latency = random.randint(1,120)
        banner = f" - banner: {hosts[target][p]}/1.0" if p in open_ports else ""
        print(f"probe -> port {p} ... rtt {latency}ms{banner}")
        slow(0.05)

    while True:
        ans = input("\nEnter suspected open ports (comma-separated): ").strip()
        parts = [p.strip() for p in ans.replace(" ","").split(",") if p.strip().isdigit()]
        guessed = sorted(int(p) for p in parts)
        if guessed == open_ports:
            print("\n✅ Correct ports identified.")
            action = input("Action (secure/probe/ignore): ").strip().lower()
            if action == "secure":
                print("\nTarget secured! +150 XP")
                xp += 150
            elif action == "probe":
                print("\nIntel gathered! +120 XP")
                xp += 120
            elif action == "ignore":
                print("\nNo action taken. +60 XP")
                xp += 60
            save_progress(username, xp)
            return xp
        else:
            print("❌ Not correct. Try again.")
