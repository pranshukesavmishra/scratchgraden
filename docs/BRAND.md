# GradeNext brand — as applied to the platform

Taken from the official **GradeNext Branding Kit** (`docs/GradeNext-Branding-Kit.pdf`).
All values below are the ones wired into `assets/css/styles.css` (`:root`).

## Typeface
**Poppins** — Bold/SemiBold for headings, Medium/Regular for body and UI.
Loaded from Google Fonts on every page.

## Main colour
| Token | Hex | Use |
|---|---|---|
| `--gn-purple` | `#703D84` | primary brand colour |
| `--gn-purple-dark` | `#5A2F6B` | pressed / dark states |
| `--gn-purple-deep` | `#2D1151` | headings, deep ink |
| `--gn-purple-mid` | `#8D4DA5` | ramp |
| `--gn-purple-light` | `#A169B7` | ramp |
| `--gn-purple-pale` | `#DAC2E3` | ramp |
| `--gn-purple-wash` | `#EDE1F1` | tints, surfaces |

## Accent
| Token | Hex | Use |
|---|---|---|
| `--gn-pink` | `#F5007E` | the signature rule under headings, kickers |

## Secondary palette (pastels)
`#FBBE95` peach · `#9ECCFA` blue · `#FBDD80` yellow · `#D2BBFB` lavender ·
`#F8B3CF` pink · `#89E6D5` mint

## Gradients
| Token | Value |
|---|---|
| `--grad-brand` | `#7F5DF9 → #A855F7 → #FF6AC6` |
| `--grad-deep` | `#2D1151 → #5A2F6B → #703D84` |
| `--grad-brand-soft` | translucent violet → magenta |

Other brand gradients from the kit: `#8DBBFF→#CDE6FF`, `#C8B6FF→#EAE2FF`,
`#9FF5D0→#D8FFF2`, `#FFB6D9→#FFE3F1`, `#FFE68B→#FFF8FF`, `#FFCC9C→#FFE8D2`.

## Neutrals
`--gn-bg #F9FAFB` · `--gn-surface #FFFFFF` · `--gn-border #E9E2EF` ·
text `#2D1151` / `#5B4A6B` / `#8E80A0`

## Technical gloss layer
A "TECH GLOSS" block in `styles.css` gives the brand a technical, glossy
finish without altering any brand hue: gradient primary buttons with a
specular highlight and glow, glass cards (`backdrop-filter`), gradient
progress bars with a bloom, gradient-filled statistic numbers, and a subtle
sheen on Scratch blocks.

> **Scratch block colours are deliberately NOT re-branded.** Motion blue,
> Control orange, Looks purple etc. must match real Scratch so children can
> transfer what they learn. They only receive the gloss treatment.
