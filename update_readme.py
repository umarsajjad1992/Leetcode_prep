import os

categories = [
    "Arrays",
    "Strings",
    "LinkedLists",
    "Trees",
    "Graphs",
    "DynamicProgramming",
    "Math"
]

def count_py_files(folder):
    if not os.path.exists(folder):
        return 0
    return sum(1 for f in os.listdir(folder) if f.endswith(".py"))

# Read README
with open("README.md", "r", encoding="utf-8") as file:
    lines = file.readlines()

start = lines.index("<!-- STATS_START -->\n")
end = lines.index("<!-- STATS_END -->\n")

# Rebuild stats table
stats_table = "| Topic | Solved |\n|-------|--------|\n"
for topic in categories:
    count = count_py_files(topic)
    stats_table += f"| {topic} | {count} |\n"

# Replace stats section
lines[start+1:end] = [stats_table]

with open("README.md", "w", encoding="utf-8") as file:
    file.writelines(lines)
