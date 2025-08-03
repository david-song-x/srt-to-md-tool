import matplotlib.pyplot as plt
from pathlib import Path

# Output file name
output_file = Path("flowchart.png")

# Create the diagram
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis("off")

# Diagram elements
elements = [
    ("Input Folder\n(with .srt files)", (0.5, 0.9)),
    ("Recursive Search\n(all subfolders)", (0.5, 0.75)),
    ("Clean & Merge Text\n(remove timestamps & numbers)", (0.5, 0.6)),
    ("Choice of Script", (0.5, 0.45)),
    ("srt_to_md.py\nFull Workflow:\n• Article\n• Summary\n• Comparisons\n• Highlights", (0.2, 0.25)),
    ("srt_to_text.py\nLightweight:\n• Clean Transcript only", (0.8, 0.25)),
    ("Outputs Saved\n1. Next to original\n2. In mirrored 'output' folder", (0.5, 0.05))
]

# Draw boxes
for text, (x, y) in elements:
    ax.text(x, y, text, ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.5", fc="lightblue", ec="black", lw=1),
            fontsize=9)

# Draw arrows
arrows = [
    ((0.5, 0.85), (0.5, 0.78)),
    ((0.5, 0.7), (0.5, 0.63)),
    ((0.5, 0.55), (0.5, 0.48)),
    ((0.5, 0.42), (0.25, 0.3)),
    ((0.5, 0.42), (0.75, 0.3)),
    ((0.25, 0.2), (0.5, 0.1)),
    ((0.75, 0.2), (0.5, 0.1))
]
for start, end in arrows:
    ax.annotate("", xy=end, xytext=start, arrowprops=dict(arrowstyle="->", lw=1.5))

# Save the flowchart
plt.savefig(output_file, bbox_inches="tight")
print(f"Flowchart saved to: {output_file.resolve()}")
