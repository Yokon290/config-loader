import json

try:
    with open("settings.json", "r") as file:
        config = json.load(file)
    
    print("✅ App Configuration Loaded!")
    print("-----------------------------")
    print(f"App Name   :{config['app_name']}")
    print(f"Version    :{config['version']}")
    print(f"Debug Mode :{config['debug_mode']}")
    print(f"Max Users  :{config['max_users']}")

except FileNotFoundError:
    print("❌ settings.json file is missing!")
except json.JSONDecodeError:
    print("❌ settings.json contains invalid JSON!")
except KeyError as e:
    print("Missing Key in config: {e}")
finally:
    print("📦 Done reading config.")

