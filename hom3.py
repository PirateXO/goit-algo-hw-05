

import sys
import re
from typing import List, Dict, Callable


''' Функції для аналізу лог-файлів
 Функція `parse_log_line` '''

def parse_log_line(line: str) -> dict:
    match = re.match(r'(\S+ \S+) (\w+) (.+)', line)
    if match:
        return {
            'timestamp': match.group(1),
            'level': match.group(2),
            'message': match.group(3)
        }
    else:
        return {}

''' Функція `load_logs` '''


def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line.strip())
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)
    return logs

''' Функція `filter_logs_by_level`'''

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return [log for log in logs if log['level'].upper() == level.upper()]

'''функція сount_logs_by_level'''

def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts = {}
    for log in logs:
        level = log['level'].upper()
        counts[level] = counts.get(level, 0) + 1
    return counts


''' Функція `display_log_counts` '''


def display_log_counts(counts: Dict[str, int]):
    print("Log Levels Count:")
    for level, count in counts.items():
        print(f"{level}: {count}")


'''  Основна функція скрипта'''


def main():
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <log_file_path> [log_level]")
        sys.exit(1)
    
    log_file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(log_file_path)
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        for log in filtered_logs:
            print(f"{log['timestamp']} {log['level']} {log['message']}")
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

if __name__ == "__main__":
    main()

