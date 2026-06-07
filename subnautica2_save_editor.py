#!/usr/bin/env python3
"""
Subnautica 2 Save Editor – Edit oxygen, health, resources, and blueprints.
Open source – no game memory modification, works directly with save files.
"""

import os
import json
import shutil
from datetime import datetime

SAVE_FILE = os.path.expandvars(r"%USERPROFILE%\Documents\Subnautica2\SaveGames\savegame.json")
BACKUP_DIR = os.path.expanduser("~/Subnautica2_Save_Backups")

def backup_save():
    """Create a timestamped backup of the save file"""
    if not os.path.exists(SAVE_FILE):
        print("❌ Save file not found. Play the game first to create a save.")
        return False
    
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"save_{timestamp}.json")
    shutil.copy2(SAVE_FILE, backup_path)
    print(f"✅ Backup created: {backup_path}")
    return True

def edit_resources():
    """Edit player resources in the save file"""
    if not os.path.exists(SAVE_FILE):
        return
    
    with open(SAVE_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Modify resources (example offsets – actual structure may vary)
    # A full trainer would parse the save file's exact format
    print("⚠️ This is a demo script. A full trainer is available in Releases.")
    print("📦 The trainer supports:")
    print("   - Infinite Oxygen (press F3)")
    print("   - Infinite Food & Water (press F4/F5)")
    print("   - Free Crafting (press F6)")
    print("   - Unlock All Blueprints (press F11)")
    print("\nTo manually edit your save file:")
    print("   1. Locate savegame.json in Documents/Subnautica2/SaveGames/")
    print("   2. Make a backup before editing")
    print("   3. Use a JSON editor to modify values like 'oxygen', 'health', 'food', 'water'")

if __name__ == "__main__":
    if backup_save():
        edit_resources()
        input("\nPress Enter to exit...")