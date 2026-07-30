# -*- coding: utf-8 -*-
"""
SVG costume + backdrop art for the Scratch starter projects.
Each sprite costume is a 100x100 SVG centred at (50,50) unless noted with an
explicit centre. Backdrops are 480x360 centred at (240,180).
Kept deliberately simple, bright and recognisable for ages 7-12.
"""

# name -> (svg_string, rotationCenterX, rotationCenterY)
SPRITES = {}
# name -> svg_string  (all 480x360, centre 240,180)
BACKDROPS = {}


def _s(name, svg, cx=50, cy=50):
    SPRITES[name] = (svg.strip(), cx, cy)


# ---- Player / hero (friendly cat-like character) ----
_s("Hero", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <ellipse cx="50" cy="88" rx="26" ry="7" fill="#000" opacity="0.12"/>
  <path d="M28 30 L20 10 L38 24 Z" fill="#ff8c1a" stroke="#c96a00" stroke-width="2"/>
  <path d="M72 30 L80 10 L62 24 Z" fill="#ff8c1a" stroke="#c96a00" stroke-width="2"/>
  <circle cx="50" cy="52" r="30" fill="#ffb14d" stroke="#c96a00" stroke-width="3"/>
  <circle cx="40" cy="48" r="5.5" fill="#2b2b2b"/>
  <circle cx="60" cy="48" r="5.5" fill="#2b2b2b"/>
  <circle cx="41.5" cy="46.5" r="1.8" fill="#fff"/>
  <circle cx="61.5" cy="46.5" r="1.8" fill="#fff"/>
  <path d="M44 62 Q50 68 56 62" fill="none" stroke="#7a4a00" stroke-width="3" stroke-linecap="round"/>
  <circle cx="50" cy="58" r="3" fill="#e8663d"/>
</svg>""")

# ---- Collectibles ----
_s("Apple", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <path d="M50 30 q10 -12 20 -6" fill="none" stroke="#5a8f2b" stroke-width="6" stroke-linecap="round"/>
  <rect x="47" y="18" width="6" height="16" rx="3" fill="#7a4a00"/>
  <path d="M50 30 C25 22 18 55 32 74 C40 86 60 86 68 74 C82 55 75 22 50 30 Z" fill="#e0483d" stroke="#a3271f" stroke-width="3"/>
  <ellipse cx="40" cy="46" rx="6" ry="9" fill="#fff" opacity="0.35"/>
</svg>""")

_s("Gem", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <polygon points="50,16 78,40 50,86 22,40" fill="#9966ff" stroke="#5a3ec0" stroke-width="3"/>
  <polygon points="50,16 78,40 50,44 22,40" fill="#c3aaff"/>
  <polygon points="22,40 50,44 50,86" fill="#7a52e0"/>
</svg>""", 50, 50)

_s("Coin", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="34" fill="#ffcf33" stroke="#d69a00" stroke-width="4"/>
  <circle cx="50" cy="50" r="24" fill="none" stroke="#ffe58a" stroke-width="3"/>
  <text x="50" y="64" font-size="34" font-family="sans-serif" font-weight="bold" fill="#b57d00" text-anchor="middle">$</text>
</svg>""")

_s("Star", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <polygon points="50,12 61,40 92,40 66,58 76,88 50,70 24,88 34,58 8,40 39,40"
    fill="#ffd21a" stroke="#e0a500" stroke-width="3" stroke-linejoin="round"/>
</svg>""")

_s("Flag", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <rect x="30" y="10" width="5" height="80" rx="2" fill="#6b6b6b"/>
  <path d="M35 12 H80 V44 H35 Z" fill="#fff" stroke="#333" stroke-width="1"/>
  <g fill="#333">
    <rect x="35" y="12" width="11" height="8"/><rect x="57" y="12" width="12" height="8"/>
    <rect x="46" y="20" width="11" height="8"/><rect x="69" y="20" width="11" height="8"/>
    <rect x="35" y="28" width="11" height="8"/><rect x="57" y="28" width="12" height="8"/>
    <rect x="46" y="36" width="11" height="8"/><rect x="69" y="36" width="11" height="8"/>
  </g>
</svg>""", 32, 88)

_s("Basket", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <path d="M16 40 H84 L74 82 H26 Z" fill="#c98a3a" stroke="#8a5a1e" stroke-width="3"/>
  <path d="M24 30 Q50 6 76 30" fill="none" stroke="#8a5a1e" stroke-width="5"/>
  <g stroke="#8a5a1e" stroke-width="2" opacity="0.7">
    <line x1="34" y1="40" x2="30" y2="82"/><line x1="50" y1="40" x2="50" y2="82"/><line x1="66" y1="40" x2="70" y2="82"/>
    <line x1="20" y1="54" x2="80" y2="54"/><line x1="22" y1="68" x2="78" y2="68"/>
  </g>
</svg>""", 50, 50)

# ---- Minecraft-flavoured ----
_s("Creeper", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <rect x="26" y="18" width="48" height="48" rx="3" fill="#5fd35f" stroke="#3a8f3a" stroke-width="2"/>
  <rect x="30" y="66" width="40" height="20" rx="3" fill="#4bb84b" stroke="#3a8f3a" stroke-width="2"/>
  <rect x="34" y="30" width="12" height="12" fill="#1f1f1f"/>
  <rect x="54" y="30" width="12" height="12" fill="#1f1f1f"/>
  <path d="M44 44 h12 v10 h-6 v8 h-12 v-8 h6 z" fill="#1f1f1f"/>
</svg>""", 50, 52)

_s("Villager", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <rect x="32" y="52" width="36" height="36" rx="3" fill="#6b4a2f" stroke="#4a3320" stroke-width="2"/>
  <rect x="34" y="16" width="32" height="40" rx="4" fill="#c9a17a" stroke="#8a6a4a" stroke-width="2"/>
  <rect x="45" y="34" width="10" height="22" rx="4" fill="#a9825f"/>
  <rect x="38" y="30" width="7" height="7" fill="#2b2b2b"/>
  <rect x="55" y="30" width="7" height="7" fill="#2b2b2b"/>
</svg>""", 50, 52)

# ---- Flappy bird set ----
_s("Bird", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <ellipse cx="50" cy="54" rx="30" ry="26" fill="#ffd21a" stroke="#e0a500" stroke-width="3"/>
  <path d="M22 54 q-14 -2 -18 8 q16 6 20 -2 z" fill="#ffb800" stroke="#e0a500" stroke-width="2"/>
  <circle cx="62" cy="44" r="8" fill="#fff" stroke="#333" stroke-width="2"/>
  <circle cx="64" cy="44" r="3.5" fill="#000"/>
  <path d="M76 52 l16 -4 -14 12 z" fill="#ff8c1a" stroke="#c96a00" stroke-width="2"/>
</svg>""", 50, 54)

_s("Pipe", """
<svg xmlns="http://www.w3.org/2000/svg" width="80" height="240" viewBox="0 0 80 240">
  <rect x="14" y="30" width="52" height="210" fill="#4bb84b" stroke="#2f7d2f" stroke-width="3"/>
  <rect x="6" y="4" width="68" height="34" rx="4" fill="#5fd35f" stroke="#2f7d2f" stroke-width="3"/>
  <rect x="22" y="34" width="8" height="206" fill="#7de07d" opacity="0.6"/>
</svg>""", 40, 120)

_s("Platform", """
<svg xmlns="http://www.w3.org/2000/svg" width="140" height="36" viewBox="0 0 140 36">
  <rect x="1" y="10" width="138" height="24" rx="3" fill="#9a6a3a" stroke="#6b4a2a" stroke-width="2"/>
  <rect x="1" y="4" width="138" height="12" rx="3" fill="#6fbf4a" stroke="#4a8f2f" stroke-width="2"/>
</svg>""", 70, 18)

# ---- Pong / Breakout ----
_s("Paddle", """
<svg xmlns="http://www.w3.org/2000/svg" width="110" height="24" viewBox="0 0 110 24">
  <rect x="2" y="4" width="106" height="16" rx="8" fill="#4c97ff" stroke="#2f6fd6" stroke-width="2"/>
  <rect x="10" y="7" width="90" height="4" rx="2" fill="#a9ccff"/>
</svg>""", 55, 12)

_s("Ball", """
<svg xmlns="http://www.w3.org/2000/svg" width="44" height="44" viewBox="0 0 44 44">
  <circle cx="22" cy="22" r="18" fill="#ffffff" stroke="#8a94a6" stroke-width="3"/>
  <circle cx="16" cy="16" r="5" fill="#eef2fa"/>
</svg>""", 22, 22)

_s("Brick", """
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="28" viewBox="0 0 64 28">
  <rect x="1" y="1" width="62" height="26" rx="3" fill="#e0483d" stroke="#a3271f" stroke-width="2"/>
  <rect x="6" y="5" width="52" height="6" rx="2" fill="#ff8a80" opacity="0.7"/>
</svg>""", 32, 14)

# ---- Enemies / hazards ----
_s("Enemy", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <ellipse cx="50" cy="60" rx="30" ry="26" fill="#8a5a2b" stroke="#5f3d1c" stroke-width="3"/>
  <rect x="30" y="80" width="16" height="12" rx="3" fill="#3a2610"/>
  <rect x="54" y="80" width="16" height="12" rx="3" fill="#3a2610"/>
  <ellipse cx="40" cy="54" rx="7" ry="9" fill="#fff"/><ellipse cx="60" cy="54" rx="7" ry="9" fill="#fff"/>
  <circle cx="41" cy="56" r="3" fill="#000"/><circle cx="59" cy="56" r="3" fill="#000"/>
  <path d="M33 44 l14 6 M67 44 l-14 6" stroke="#3a2610" stroke-width="3" stroke-linecap="round"/>
</svg>""", 50, 56)

_s("Spikes", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="60" viewBox="0 0 100 60">
  <polygon points="6,58 20,10 34,58" fill="#c0392b" stroke="#7d241a" stroke-width="2"/>
  <polygon points="33,58 50,6 67,58" fill="#c0392b" stroke="#7d241a" stroke-width="2"/>
  <polygon points="66,58 80,10 94,58" fill="#c0392b" stroke="#7d241a" stroke-width="2"/>
</svg>""", 50, 30)

# ---- Space shooter ----
_s("Ship", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <polygon points="50,10 74,74 50,60 26,74" fill="#5cb1d6" stroke="#2f7ea0" stroke-width="3"/>
  <circle cx="50" cy="42" r="9" fill="#d7f0ff" stroke="#2f7ea0" stroke-width="2"/>
  <polygon points="34,66 26,86 44,70" fill="#ff8c1a"/>
  <polygon points="66,66 74,86 56,70" fill="#ff8c1a"/>
</svg>""", 50, 48)

_s("Bullet", """
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="48" viewBox="0 0 24 48">
  <rect x="8" y="4" width="8" height="40" rx="4" fill="#59c059" stroke="#2f8f2f" stroke-width="2"/>
  <circle cx="12" cy="8" r="6" fill="#b7f0b7"/>
</svg>""", 12, 24)

_s("Alien", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <ellipse cx="50" cy="50" rx="30" ry="24" fill="#9966ff" stroke="#5a3ec0" stroke-width="3"/>
  <circle cx="38" cy="48" r="8" fill="#fff"/><circle cx="62" cy="48" r="8" fill="#fff"/>
  <circle cx="38" cy="48" r="3.5" fill="#1f1f1f"/><circle cx="62" cy="48" r="3.5" fill="#1f1f1f"/>
  <path d="M30 72 q8 8 20 0 q10 8 20 0" fill="none" stroke="#5a3ec0" stroke-width="3"/>
  <line x1="40" y1="26" x2="34" y2="14" stroke="#5a3ec0" stroke-width="3"/><circle cx="33" cy="12" r="3" fill="#5a3ec0"/>
  <line x1="60" y1="26" x2="66" y2="14" stroke="#5a3ec0" stroke-width="3"/><circle cx="67" cy="12" r="3" fill="#5a3ec0"/>
</svg>""", 50, 50)

# ---- Clicker / tycoon ----
_s("Cookie", """
<svg xmlns="http://www.w3.org/2000/svg" width="120" height="120" viewBox="0 0 120 120">
  <circle cx="60" cy="60" r="50" fill="#c98a3a" stroke="#8a5a1e" stroke-width="4"/>
  <g fill="#5a3a18">
    <circle cx="44" cy="42" r="7"/><circle cx="78" cy="50" r="6"/><circle cx="56" cy="72" r="7"/>
    <circle cx="82" cy="80" r="5"/><circle cx="38" cy="70" r="5"/><circle cx="66" cy="34" r="4"/>
  </g>
</svg>""", 60, 60)

# ---- Dancers ----
_s("Dancer1", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <circle cx="50" cy="24" r="12" fill="#ffb14d" stroke="#c96a00" stroke-width="2"/>
  <rect x="42" y="36" width="16" height="30" rx="6" fill="#e0483d"/>
  <path d="M42 42 L24 34 M58 42 L76 30" stroke="#e0483d" stroke-width="6" stroke-linecap="round"/>
  <path d="M46 66 L34 88 M54 66 L66 88" stroke="#4c97ff" stroke-width="7" stroke-linecap="round"/>
</svg>""", 50, 56)

_s("Dancer2", """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <circle cx="50" cy="24" r="12" fill="#c9a17a" stroke="#8a6a4a" stroke-width="2"/>
  <rect x="42" y="36" width="16" height="30" rx="6" fill="#9966ff"/>
  <path d="M42 44 L26 52 M58 40 L74 44" stroke="#9966ff" stroke-width="6" stroke-linecap="round"/>
  <path d="M46 66 L36 90 M54 66 L70 84" stroke="#59c059" stroke-width="7" stroke-linecap="round"/>
</svg>""", 50, 56)


# =====================  BACKDROPS  =====================
BACKDROPS["Plain"] = """
<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
  <defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#eaf3ff"/><stop offset="1" stop-color="#f7fbff"/></linearGradient></defs>
  <rect width="480" height="360" fill="url(#g)"/>
</svg>"""

BACKDROPS["Sky"] = """
<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
  <defs><linearGradient id="s" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#6ec3ff"/><stop offset="1" stop-color="#bfe6ff"/></linearGradient></defs>
  <rect width="480" height="360" fill="url(#s)"/>
  <g fill="#ffffff" opacity="0.9">
    <ellipse cx="110" cy="80" rx="46" ry="24"/><ellipse cx="150" cy="80" rx="34" ry="20"/>
    <ellipse cx="360" cy="120" rx="40" ry="22"/><ellipse cx="395" cy="120" rx="30" ry="18"/>
  </g>
  <rect y="312" width="480" height="48" fill="#6fbf4a"/>
  <rect y="312" width="480" height="12" fill="#8ad06a"/>
</svg>"""

BACKDROPS["Space"] = """
<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
  <rect width="480" height="360" fill="#0d1030"/>
  <g fill="#ffffff">
    <circle cx="60" cy="50" r="2"/><circle cx="140" cy="90" r="1.5"/><circle cx="220" cy="40" r="2"/>
    <circle cx="300" cy="80" r="1.5"/><circle cx="380" cy="50" r="2"/><circle cx="440" cy="120" r="1.5"/>
    <circle cx="100" cy="200" r="1.5"/><circle cx="200" cy="260" r="2"/><circle cx="330" cy="220" r="1.5"/>
    <circle cx="420" cy="280" r="2"/><circle cx="40" cy="300" r="1.5"/><circle cx="260" cy="150" r="1.5"/>
  </g>
  <circle cx="400" cy="300" r="46" fill="#3a3f7a" opacity="0.8"/>
</svg>"""

BACKDROPS["Maze"] = """
<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
  <rect width="480" height="360" fill="#f4f8ff"/>
  <g fill="#2f6fd6">
    <rect x="0" y="0" width="480" height="16"/><rect x="0" y="344" width="480" height="16"/>
    <rect x="0" y="0" width="16" height="360"/><rect x="464" y="0" width="16" height="360"/>
    <rect x="96" y="16" width="16" height="180"/><rect x="96" y="180" width="150" height="16"/>
    <rect x="200" y="80" width="16" height="130"/><rect x="200" y="80" width="130" height="16"/>
    <rect x="330" y="80" width="16" height="200"/><rect x="360" y="250" width="104" height="16"/>
    <rect x="96" y="260" width="180" height="16"/>
  </g>
</svg>"""

BACKDROPS["Dungeon"] = """
<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
  <rect width="480" height="360" fill="#2b2f3a"/>
  <g fill="#3a4150" stroke="#232833" stroke-width="2">
    <rect x="10" y="10" width="70" height="46"/><rect x="90" y="10" width="70" height="46"/>
    <rect x="170" y="10" width="70" height="46"/><rect x="250" y="10" width="70" height="46"/>
    <rect x="330" y="10" width="70" height="46"/><rect x="410" y="10" width="60" height="46"/>
  </g>
  <rect y="300" width="480" height="60" fill="#4a4030"/>
  <rect y="300" width="480" height="10" fill="#5c5038"/>
</svg>"""

BACKDROPS["Stage"] = """
<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
  <rect width="480" height="360" fill="#16122b"/>
  <polygon points="120,0 60,360 200,360 180,0" fill="#ffd21a" opacity="0.14"/>
  <polygon points="360,0 300,360 440,360 420,0" fill="#ff6fae" opacity="0.14"/>
  <rect y="300" width="480" height="60" fill="#3a2a1a"/>
  <rect y="300" width="480" height="8" fill="#5a4028"/>
</svg>"""

BACKDROPS["Grass"] = """
<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
  <rect width="480" height="360" fill="#7ec850"/>
  <rect width="480" height="120" fill="#8ad06a"/>
  <g fill="#5a3a1e">
    <ellipse cx="120" cy="150" rx="46" ry="18"/><ellipse cx="300" cy="130" rx="46" ry="18"/>
    <ellipse cx="200" cy="250" rx="46" ry="18"/><ellipse cx="380" cy="260" rx="46" ry="18"/>
  </g>
</svg>"""
