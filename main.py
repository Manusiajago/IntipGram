# main.py

import json
import os
import sys
from datetime import datetime

# ASCII Banner for IntipGram
BANNER = r"""
 █████             █████     ███              █████████                                     
░░███             ░░███     ░░░              ███░░░░░███                                    
 ░███  ████████   ███████   ████  ████████  ███     ░░░  ████████   ██████   █████████████  
 ░███ ░░███░░███ ░░░███░   ░░███ ░░███░░███░███         ░░███░░███ ░░░░░███ ░░███░░███░░███ 
 ░███  ░███ ░███   ░███     ░███  ░███ ░███░███    █████ ░███ ░░░   ███████  ░███ ░███ ░███ 
 ░███  ░███ ░███   ░███ ███ ░███  ░███ ░███░░███  ░░███  ░███      ███░░███  ░███ ░███ ░███ 
 █████ ████ █████  ░░█████  █████ ░███████  ░░█████████  █████    ░░████████ █████░███ █████
░░░░░ ░░░░ ░░░░░    ░░░░░  ░░░░░  ░███░░░    ░░░░░░░░░  ░░░░░      ░░░░░░░░ ░░░░░ ░░░ ░░░░░ 
                                  ░███                                                      
                                  █████                                                     
                                 ░░░░░               
"""

def display_banner():
    print(BANNER)

def get_file_path(prompt):
    return input(prompt).strip()

def load_json_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in the file.")
    except Exception as e:
        raise RuntimeError(f"Error reading file: {str(e)}")

def extract_instagram_list(data, is_following=False):
    # For Instagram structures like followers/following
    items = []
    if is_following and isinstance(data, dict) and "relationships_following" in data:
        data = data["relationships_following"]
    for entry in data:
        if "string_list_data" in entry and isinstance(entry["string_list_data"], list) and entry["string_list_data"]:
            item_data = entry["string_list_data"][0]
            timestamp = item_data.get("timestamp", "")
            try:
                dt = datetime.fromtimestamp(int(timestamp))
                date_str = dt.strftime("%Y-%m-%d %H:%M:%S")
            except:
                date_str = timestamp
            items.append({
                "username": item_data.get("value", ""),
                "date": date_str,
                "href": item_data.get("href", "")
            })
    # Sort by timestamp descending (most recent first)
    items.sort(key=lambda x: x.get("date", ""), reverse=True)
    return items

def print_table(data_list, headers=None, title=""):
    if not data_list:
        return
    if headers is None:
        headers = list(data_list[0].keys())
    if title:
        print(f"\n{title}")
    rows = [[str(item.get(h, '')) for h in headers] for item in data_list]
    # Truncate long cells for better display
    max_width = 40
    rows = [[cell[:max_width] + '...' if len(cell) > max_width else cell for cell in row] for row in rows]
    headers = [h[:max_width] for h in headers]
    # Calculate column widths
    widths = [max(len(cell) for cell in col) for col in zip(headers, *rows)]
    # Print top border
    print('+' + '+'.join('-' * (w + 2) for w in widths) + '+')
    # Print headers
    print('| ' + ' | '.join(h.ljust(w) for h, w in zip(headers, widths)) + ' |')
    # Print separator
    print('+' + '+'.join('-' * (w + 2) for w in widths) + '+')
    # Print rows
    for row in rows:
        print('| ' + ' | '.join(c.ljust(w) for c, w in zip(row, widths)) + ' |')
    # Print bottom border
    print('+' + '+'.join('-' * (w + 2) for w in widths) + '+')

def analyze_and_compare(followers_data, following_data):
    print("\n=== Analyzing Instagram Data ===\n")
    
    followers = extract_instagram_list(followers_data)
    following = extract_instagram_list(following_data, is_following=True)
    
    followers_set = set(item['username'] for item in followers)
    following_set = set(item['username'] for item in following)
    
    # Unfollowers: people you follow but who don't follow you back
    unfollowers_set = following_set - followers_set
    unfollowers = [item for item in following if item['username'] in unfollowers_set]
    
    # Mutual follows: intersection
    mutual = followers_set & following_set
    
    print(f"Total Followers: {len(followers)}")
    print(f"Total Following: {len(following)}")
    print(f"Mutual Follows: {len(mutual)}")
    print(f"Unfollowers (You follow them, but they don't follow back): {len(unfollowers)}")
    
    # Display tables
    print_table(followers, headers=["username", "date", "href"], title="Followers:")
    print_table(following, headers=["username", "date", "href"], title="Following:")
    print_table(unfollowers, headers=["username", "date", "href"], title="Unfollowers:")

def main():
    display_banner()
    try:
        followers_path = get_file_path("Enter the path to your followers JSON file (e.g., followers_1.json): ")
        following_path = get_file_path("Enter the path to your following JSON file (e.g., following.json): ")
        
        followers_data = load_json_file(followers_path)
        following_data = load_json_file(following_path)
        
        analyze_and_compare(followers_data, following_data)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()