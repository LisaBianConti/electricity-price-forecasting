import matplotlib.pyplot as plt
import seaborn as sns

COLORS = {
    "primary": "#0F4C5C",
    "secondary": "#6D9DC5",
    "accent": "#FF7F50",
    "crisis": "#EF4026"
}

PRIMARY = "#0F4C5C"
SECONDARY = "#6D9DC5"
ACCENT = "#E36414"
BACKGROUND = "#FAFAFA"
TEXT = "#222222"
GRID = "#BBBBBB"

def apply_style():
    plt.style.use("default")

    plt.rcParams.update(
        {
        "font.family": "DejaVu Sans",
        "font.size": 12,

        "figure.figsize": (10, 5),
        "figure.facecolor": BACKGROUND,
        "axes.facecolor": BACKGROUND,

        "text.color": TEXT,
        "axes.labelcolor": TEXT,
        "xtick.color": TEXT,
        "ytick.color": TEXT,

        "axes.titlesize": 16,
        "axes.titleweight": "bold",
        "axes.labelsize": 13,
        "axes.edgecolor": "#333333",
        "axes.linewidth": 1,

        "axes.grid": True,
        "grid.alpha": 0.2,
        "grid.color": GRID,

        "legend.frameon": False
        
        }
    )

sns.set_style("white")
