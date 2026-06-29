import subprocess
import re

# Get saved Wi-Fi profiles
data = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles"],
    text=True,
    encoding="utf-8",
    errors="ignore"
)

profiles = re.findall(r"All User Profile\s*:\s(.*)", data)

print("Saved Wi-Fi Profiles:\n")

for profile in profiles:
    print(f"SSID: {profile}")

    try:
        details = subprocess.check_output(
            ["netsh", "wlan", "show", "profile", profile, "key=clear"],
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        password_match = re.search(r"Key Content\s*:\s(.*)", details)

        if password_match:
            print("Password:", password_match.group(1))
        else:
            print("Password: Not Stored")

    except Exception:
        print("Password: Unable to Read")

    print("-" * 40)