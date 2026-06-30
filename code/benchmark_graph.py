import matplotlib.pyplot as plt
import numpy as np

# Data #

models = [
    "Llama 3.1 8B",
    "Mistral 7B",
    "Qwen 2.5 7B",
    "ChatGPT",
    "Claude"
]

accuracy = [57.50, 29.00, 73.75, 95.00, 98.75]

reasoning_quality = [82.08, 63.75, 82.08, 87.50, 95.42]

programming_correctness = [84.58, 57.50, 84.17, 96.25, 97.50]

reliability = [92.50, 92.50, 87.50, 96.25, 98.75]

#Graph#

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 11,
    "axes.titlesize": 12,
    "legend.fontsize": 9
})

x = np.arange(len(models))
width = 0.20

fig, ax = plt.subplots(figsize=(8, 4.5))

# Bars #

bars1 = ax.bar(
    x - 1.5 * width,
    accuracy,
    width,
    label='Accuracy',
    color='white',
    edgecolor='black',
    hatch='///'
)

bars2 = ax.bar(
    x - 0.5 * width,
    reasoning_quality,
    width,
    label='Reasoning Quality',
    color='white',
    edgecolor='black',
    hatch='\\\\\\'
)

bars3 = ax.bar(
    x + 0.5 * width,
    programming_correctness,
    width,
    label='Programming Correctness',
    color='white',
    edgecolor='black',
    hatch='xxx'
)

bars4 = ax.bar(
    x + 1.5 * width,
    reliability,
    width,
    label='Reliability',
    color='white',
    edgecolor='black',
    hatch='...'
)

# lables and Title#

ax.set_title(
    "Benchmark Evaluation Results Across Models",
    pad=12
)

ax.set_xlabel("Models")
ax.set_ylabel("Score (%)")

ax.set_xticks(x)
ax.set_xticklabels(models)

ax.set_ylim(0, 120)

ax.grid(
    axis='y',
    linestyle='--',
    linewidth=0.5,
    alpha=0.7
)

ax.legend(
    ncol=2,
    frameon=True,
    loc='upper center',
    bbox_to_anchor=(0.5, 1.01)
)

#value lables #

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f'{height:.1f}',
            xy=(bar.get_x() + bar.get_width()/2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha='center',
            va='bottom',
            fontsize=7
        )

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)
add_labels(bars4)

plt.tight_layout()


plt.savefig(
    "Benchmark_Evaluation_Results.png",
    dpi=600,
    bbox_inches='tight'
)

plt.savefig(
    "Benchmark_Evaluation_Results.pdf",
    bbox_inches='tight'
)

plt.show()