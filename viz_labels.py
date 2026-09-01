"""
Reader-friendly labels for NHL Cap Hit project charts and tables.

Use the same names in EDA.ipynb and CatBoost model notebooks so a non-technical
reader does not have to decode abbreviations.

Example
-------
from viz_labels import lab, LABELS

ax.set_ylabel(lab("CapHit_pct"))
"""

from __future__ import annotations

# Column / field -> plain English label (charts, axes, legends, tables)
LABELS: dict[str, str] = {
    # Target / pay
    "CapHit": "Cap hit ($ millions)",
    "CapHit_pct": "Share of salary cap",
    "CapHit_next": "Cap hit next season ($ millions)",
    "CapHit_pct_next": "Share of salary cap next season",
    # Identity / context
    "Player": "Player",
    "Season": "Season",
    "Team": "Team",
    "Age": "Age",
    "Age_at_signing_approx": "Age when the deal started",
    "Pos_group": "Position",
    "FD": "Position (forward or defenseman)",
    "S/C": "Shot side",
    "GP": "Games played",
    "Season_id": "Season index",
    # Contract
    "Is_ELC": "Entry-level contract",
    "ContractLength": "Contract length (years)",
    "YearsRemaining": "Years left on contract",
    "Length_next": "Contract length next season (years)",
    # Role / ice time
    "TOI/GP": "Ice time per game (minutes)",
    "Depth_TOI_rank": "Ice time rank on the team",
    "PP TOI": "Power play ice time",
    "PK TOI": "Penalty kill ice time",
    # Value
    "WAR_per_GP": "Wins above replacement per game",
    "EVO WAR": "Even-strength offense value (WAR)",
    "EVD WAR": "Even-strength defense value (WAR)",
    "PP WAR": "Power play value (WAR)",
    "PK WAR": "Penalty kill value (WAR)",
    # Offense
    "pointsPerGame": "Points per game",
    "ixG": "Individual expected goals (season total)",
    "shots": "Shots (season total)",
    "shots_per_60": "Shots per 60 minutes",
    "ixG_per_60": "Individual expected goals per 60 minutes",
    "bursts_per_60": "Skating bursts over 20 mph per 60 minutes",
    "distance_per_60": "Skating distance per 60 minutes",
    "PP_TOI_per_game": "Power play ice time per game",
    "PK_TOI_per_game": "Penalty kill ice time per game",
    # On-ice
    "xGF%": "Expected goals for share",
    "OZ Start%": "Offensive zone start share",
    "DZ Start%": "Defensive zone start share",
    "xG_diff": "Expected goals difference",
    # Defense / physical
    "Hits": "Hits",
    "HitsT": "Hits taken",
    "BkS": "Blocked shots",
    "TkA": "Takeaways",
    "GvA": "Giveaways",
    "penaltyMinutes": "Penalty minutes",
    # Team
    "Team_pointPct": "Team points percentage",
    "Team_GF_pct": "Team goals for share",
    "Team_PP%": "Team power play percentage",
    "Team_PK%": "Team penalty kill percentage",
    # NHL Edge
    "nhl_edge_skatingSpeedMax_mph": "Top skating speed (mph)",
    "nhl_edge_burstsOver20": "Skating bursts over 20 mph",
    "nhl_edge_topShotSpeed_mph": "Top shot speed (mph)",
    "nhl_edge_totalDistanceSkated_mph": "Skating distance (NHL Edge)",
    "nhl_edge_distanceMaxGame_mph": "Max skating distance in a game (NHL Edge)",
    "nhl_edge_zoneTime_offensiveZonePctg": "Share of time in the offensive zone",
    # Bio
    "heightInInches": "Height (inches)",
    "weightInPounds": "Weight (pounds)",
    # Model outputs / review tables
    "CapHit_pct_pred": "Predicted share of salary cap",
    "residual_pct": "Residual (actual minus predicted share)",
    "residual_M": "Residual ($ millions, approx.)",
    "importance": "Feature importance",
    "mean_|SHAP|": "Mean absolute SHAP",
    "shap": "Local SHAP contribution",
}

# Short category labels for legends / tick labels
CATEGORY_LABELS: dict[str, str] = {
    "F": "Forwards",
    "D": "Defensemen",
    "ELC": "Entry-level contract",
    "non-ELC": "Not entry-level",
    "Left ELC": "Signed a new deal",
    "New non-ELC deal": "Signed a new deal",
    "Stayed on ELC": "Still on entry-level deal",
    "Still ELC": "Still on entry-level deal",
    "Still ELC (in sample)": "Still on entry-level deal",
    "Out of GP>=10 sample": "Not in this sample\n(<10 GP next season)",
    "Out of sample": "Not in this sample\n(<10 GP next season)",
}

# Outcome labels for ELC transition charts (EDA plots New vs Out only)
ELC_OUTCOME_DISPLAY = {
    "New non-ELC deal": "Signed a new deal",
    "Out of GP>=10 sample": "Not in this sample\n(<10 GP next season)",
}

# ---------------------------------------------------------------------------
# Shared chart colors (EDA + model notebooks)
# Same concept => same color across the notebook.
# ---------------------------------------------------------------------------

# Contract stage
COLOR_NON_ELC = "#4682b4"  # steelblue
COLOR_ELC = "#e67e22"  # dark orange

# Position
COLOR_F = "#c45c26"  # rust
COLOR_D = "#2e8b57"  # seagreen

# Generic single-series market charts (counts, medians without a split)
COLOR_MARKET = COLOR_NON_ELC
COLOR_MARKET_LIGHT = "#b8d4e8"

# Contract length intensity (short -> long), blue family = market / non-ELC
# Index 0 = 1 year ... index 7 = 8 years. Do NOT cycle this list for longer terms.
LENGTH_COLORS = [
    "#deebf7",  # 1
    "#c6dbef",  # 2
    "#9ecae1",  # 3
    "#6baed6",  # 4
    "#4292c6",  # 5
    "#2171b5",  # 6
    "#08519c",  # 7
    "#08306b",  # 8
]

# Same length steps, tinted by position (for F/D split charts); 1..8 years
LENGTH_COLORS_BY_POS = {
    "F": [
        "#f7ebe3",
        "#f0d7c8",
        "#e8c4ae",
        "#d9a07e",
        "#c45c26",
        "#a34a1f",
        "#7a3717",
        "#5a2810",
    ],
    "D": [
        "#e8f5ee",
        "#d0eadc",
        "#b7dfcb",
        "#8fc9ab",
        "#5fa882",
        "#3d8f66",
        "#2e6b4c",
        "#1f4a35",
    ],
}

COLOR_MUTED = "#cfd4da"
WINDOW_COLORS = ["#6baed6", "#08519c"]
COLOR_POS = COLOR_NON_ELC
COLOR_NEG = "#e07470"
CMAP_LENGTH = "Blues"

SEASONS = ["23-24", "24-25", "25-26"]
LENGTH_GROUP_ORDER = ["1", "2", "3", "4-5", "6-7", "8+"]


def length_group(v) -> str:
    v = int(v)
    if v <= 1:
        return "1"
    if v == 2:
        return "2"
    if v == 3:
        return "3"
    if v <= 5:
        return "4-5"
    if v <= 7:
        return "6-7"
    return "8+"


def season_label(season) -> str:
    """Display season codes with a slash: 23-24 -> 23/24. Data keys stay hyphenated."""
    s = str(season).strip()
    parts = s.split("-")
    if len(parts) == 2 and all(p.isdigit() and len(p) == 2 for p in parts):
        return f"{parts[0]}/{parts[1]}"
    return s


def season_window_label(season_from, season_to) -> str:
    return f"{season_label(season_from)} to {season_label(season_to)}"


def length_color(years, palette: list[str] | None = None) -> str:
    """Color for a contract length in years (1..8+). Longer than 8 uses the darkest step."""
    colors = palette if palette is not None else LENGTH_COLORS
    try:
        y = int(float(years))
    except (TypeError, ValueError):
        return colors[0]
    if y < 1:
        return colors[0]
    if y > len(colors):
        return colors[-1]
    return colors[y - 1]


def length_colors_for(years_list, palette: list[str] | None = None) -> list[str]:
    return [length_color(y, palette) for y in years_list]



def lab(key: str) -> str:
    """Return a reader-friendly label for a column or category key."""
    if key in LABELS:
        return LABELS[key]
    if key in CATEGORY_LABELS:
        return CATEGORY_LABELS[key]
    if key in ELC_OUTCOME_DISPLAY:
        return ELC_OUTCOME_DISPLAY[key]
    return key


def labs(keys: list[str]) -> list[str]:
    """Map a list of keys to labels."""
    return [lab(k) for k in keys]


__all__ = [
    "LABELS",
    "lab",
    "labs",
    "SEASONS",
    "LENGTH_GROUP_ORDER",
    "length_group",
    "LENGTH_COLORS",
    "LENGTH_COLORS_BY_POS",
    "length_color",
    "length_colors_for",
    "season_label",
    "season_window_label",
    "COLOR_NON_ELC",
    "COLOR_ELC",
    "COLOR_F",
    "COLOR_D",
    "COLOR_MARKET",
    "COLOR_MARKET_LIGHT",
    "COLOR_MUTED",
    "WINDOW_COLORS",
    "COLOR_POS",
    "COLOR_NEG",
    "CMAP_LENGTH",
    "ELC_OUTCOME_DISPLAY",
]
