# Karthik Reddy Lakkireddy: portfolio

An interactive 3D portfolio about power electronics, battery management and EV charging, from the grid to the battery.

**Live site:** https://YOUR-USERNAME.github.io/portfolio/

- A 3D energy scene (grid, wind and PV, inverter, house, charging post, car with its battery and on-board charger) on the left. Each object is one of my projects.
- A scrolling profile on the right: studies, projects, certificates, tools and contact.
- A thesis simulator (`simulator.html`): an illustrative recreation of my master's thesis GUI with assumed parameters, not thesis data.

Built with plain HTML, CSS and JavaScript, and [three.js](https://threejs.org/) for the 3D scene. No framework, no tracking.

---

# How to update the portfolio

All the text lives in **one file: `content.md`**. You never edit `index.html` by hand, because it is generated.

## The everyday routine

1. Open `content.md` in any text editor (Notepad, VS Code, or the pencil icon on GitHub).
2. Change the text. Save.
3. Build the page:

   ```
   python3 build.py
   ```

   (Windows: `py build.py`.) This needs Python 3.8 or newer and nothing else. It rewrites `index.html`.
4. Upload or commit the new `index.html`. The live site updates in a minute or two.

No Python on hand? Paste your edited `content.md` into a chat with Claude and ask it to rebuild `index.html`, then upload the result.

## What you can change in content.md

| You want to | Edit this |
|---|---|
| Change your name, email or the site address | the top block, `# Site` |
| Change the headline or opening text | `## Intro` |
| Change a project (text, numbers, dates) | `## Section: grid`, `pv`, `obc`, `battery`, `charger` or `house` |
| Add or remove a number or fact in a project | the `- bold | grey` lines under `facts:` |
| Add a certificate | add a line under `items:` in `## Certificates` |
| Change tools or languages | `## Tools` |
| Change the LinkedIn preview title or text | `share_title` and `share_description` under `# Site` |

Rules that keep it working:

- Keep the six section names (`grid`, `pv`, `obc`, `battery`, `charger`, `house`). The 3D scene links each object to its section by that name.
- One value per line: `key: value`. Use `text:` more than once for several paragraphs.
- Facts and certificates are written as `bold part | grey part`. The `|` splits them.
- Comments between `<!--` and `-->` are ignored.
- If the build says a line "could not be read", that line is missing its `key:` before the text.

## What lives where

```
content.md          all the words (edit this)
build.py            turns content.md into index.html
src/template.html   the design, the 3D scene and the styling
index.html          the finished page (generated, do not edit)
simulator.html      the thesis simulator (its own file)
og-image.png        the picture LinkedIn shows in the link preview
```

To change how the 3D scene looks (colours, object sizes, names of the labels), edit `src/template.html`, then run `python3 build.py`. The labels you see when hovering are in the `NAMES` list in the script near the bottom of that file.

---

# Publishing

## GitHub Pages (free, public, no sign-in needed to view)

1. Create a free account at github.com and a **public** repository named `portfolio`.
2. Upload everything in this folder (Add file, Upload files). Keep the folder structure: `src/template.html` must stay inside `src`.
3. Open the repository's Settings, then Pages. Under "Build and deployment" choose **Deploy from a branch**, branch **main**, folder **/ (root)**, then Save.
4. After about a minute your site is at `https://YOUR-USERNAME.github.io/portfolio/`.
5. Open that address in a private browser window to check it loads without any login.
6. In `content.md`, set `site_url:` to that address, run `python3 build.py`, and upload the new `index.html`. This fills in the LinkedIn preview picture, which needs a full address.

If the repository is named `YOUR-USERNAME.github.io`, the site is at `https://YOUR-USERNAME.github.io/` instead.

## LinkedIn

1. Put the site address in a new post. The card with the picture, title and description appears from the preview settings.
2. If the card looks old or wrong, refresh it with LinkedIn's Post Inspector (search for "LinkedIn Post Inspector"), because LinkedIn remembers previews for a while.
3. Add the address to the Website field under your profile's Contact info, and to your Featured section.

## Before you make it public

- **Thesis confidentiality:** the page describes your FEV thesis. Ask your supervisor whether the 350 kW, 720 A, derating and state-of-health details may be shown.
- **Figures:** check every number against your thesis. The simulator is illustrative, and the page says so.
- **Contact details:** your email is on the page. Remove it from `content.md` (and the `email:` line) if you prefer another way to be reached.

---

*3D scene by three.js (MIT licence). Fonts: Bricolage Grotesque and Instrument Sans from Google Fonts.*
