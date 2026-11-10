#!/usr/bin/env python3
"""
build.py: turns content.md into index.html (standard library only, Python 3.8+).

    python3 build.py

Reads  content.md and src/template.html
Writes index.html (upload this file, together with simulator.html and og-image.png)
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORDER = ["grid", "pv", "obc", "battery", "charger", "house"]
LIST_KEYS = {"facts", "items"}


def esc(text):
    """Escape for HTML but keep curly quotes, dashes and so on as typed."""
    return html.escape(text, quote=False)


def attr(text):
    return html.escape(text, quote=True)


def parse(md_text):
    """Return {block name: {key: value or list}} from content.md."""
    md_text = re.sub(r"<!--.*?-->", "", md_text, flags=re.S)
    blocks, cur, name, list_key = {}, None, None, None
    for raw in md_text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("# "):
            name = "site"
            cur = blocks.setdefault(name, {})
            list_key = None
            continue
        if line.startswith("## "):
            title = line[3:].strip()
            name = title.split(":", 1)[1].strip().lower() if title.lower().startswith("section:") else title.lower()
            cur = blocks.setdefault(name, {})
            list_key = None
            continue
        if cur is None:
            continue
        if line.startswith("- ") and list_key:
            cur[list_key].append([part.strip() for part in line[2:].split("|", 1)])
            continue
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if not m:
            print(f"warning: could not read this line, ignored: {line[:70]}", file=sys.stderr)
            continue
        key, value = m.group(1), m.group(2).strip()
        if key in LIST_KEYS and not value:
            cur[key] = []
            list_key = key
        else:
            list_key = None
            if key == "text":
                cur.setdefault("text", []).append(value)
            else:
                cur[key] = value
    return blocks


def chips(value):
    items = [c.strip() for c in value.split(",") if c.strip()]
    return '<ul class="chips">' + "".join(f"<li>{esc(c)}</li>" for c in items) + "</ul>"


def project_section(key, d):
    out = [f'    <section class="card" id="s-{key}" data-obj="{key}">']
    if d.get("eyebrow"):
        out.append(f'      <p class="eyebrow">{esc(d["eyebrow"])}</p>')
    out.append(f'      <h2>{esc(d.get("title", ""))}</h2>')
    for para in d.get("text", []):
        out.append(f"      <p>{esc(para)}</p>")
    if d.get("facts"):
        rows = "".join(f"<li><b>{esc(f[0])}</b><span>{esc(f[1] if len(f) > 1 else '')}</span></li>" for f in d["facts"])
        out.append(f'      <ul class="facts">{rows}</ul>')
    if d.get("chips"):
        out.append("      " + chips(d["chips"]))
    if d.get("small"):
        out.append(f'      <p class="small">{esc(d["small"])}</p>')
    if d.get("button"):
        label, _, url = d["button"].partition("|")
        label, url = label.strip(), url.strip()
        ext = "" if url.startswith("mailto:") else ' target="_blank" rel="noopener"'
        out.append(f'      <p><a class="btn" href="{attr(url)}"{ext}>{esc(label)}</a></p>')
    if d.get("button_note"):
        out.append(f'      <p class="small">{esc(d["button_note"])}</p>')
    out.append("    </section>")
    return "\n".join(out)


def certs_section(d):
    out = ['    <section class="card" id="s-certs">']
    out.append(f'      <p class="eyebrow">{esc(d.get("eyebrow", ""))}</p>')
    out.append(f'      <h2>{esc(d.get("title", ""))}</h2>')
    for para in d.get("text", []):
        out.append(f"      <p>{esc(para)}</p>")
    lis = "".join(f"<li><b>{esc(i[0])}</b><br><span>{esc(i[1] if len(i) > 1 else '')}</span></li>" for i in d.get("items", []))
    out.append(f'      <ul class="certs" id="certlist">{lis}</ul>')
    if d.get("small"):
        out.append(f'      <p class="small">{esc(d["small"])}</p>')
    out.append("    </section>")
    return "\n".join(out)


def tools_section(d):
    out = ['    <section class="card" id="s-tools">']
    out.append(f'      <p class="eyebrow">{esc(d.get("eyebrow", ""))}</p>')
    out.append(f'      <h2>{esc(d.get("title", ""))}</h2>')
    if d.get("chips"):
        out.append("      " + chips(d["chips"]))
    paras = "".join(f"<p>{esc(p)}</p>" for p in d.get("text", []))
    out.append(f'      <div class="grid2">{paras}</div>')
    if d.get("small"):
        out.append(f'      <p class="small">{esc(d["small"])}</p>')
    out.append("    </section>")
    return "\n".join(out)


def contact_section(d, site):
    email = site.get("email", "")
    year = d.get("year", "2026")
    out = ['    <section class="card contact" id="s-contact">']
    out.append(f'      <p class="eyebrow">{esc(d.get("eyebrow", ""))}</p>')
    out.append(f'      <h2>{esc(d.get("title", ""))}</h2>')
    out.append(f'      <p><a class="mail" href="mailto:{attr(email)}">{esc(email)}</a></p>')
    for para in d.get("text", []):
        out.append(f'      <p class="small">{esc(para)}</p>')
    out.append(f'      <footer>© {esc(year)} {esc(site.get("name", ""))}. Personal portfolio.</footer>')
    out.append("    </section>")
    return "\n".join(out)


def intro(d):
    return "\n".join([
        '    <div class="intro">',
        f'      <span class="avail">{esc(d.get("availability", ""))}</span>',
        f'      <h1>{esc(d.get("headline", ""))}</h1>',
        f'      <p>{esc(d.get("lead", ""))}</p>',
        f'      <p class="strong">{esc(d.get("note", ""))}</p>',
        "    </div>",
    ])


def main():
    blocks = parse((ROOT / "content.md").read_text(encoding="utf-8"))
    site = blocks.get("site", {})
    for need in ("name", "email", "site_url"):
        if not site.get(need):
            sys.exit(f"content.md is missing '{need}:' under '# Site'.")
    for key in ORDER:
        if key not in blocks:
            sys.exit(f"content.md is missing the block '## Section: {key}'.")

    parts = [intro(blocks.get("intro", {}))]
    parts += [project_section(k, blocks[k]) for k in ORDER]
    parts += [certs_section(blocks.get("certificates", {})), tools_section(blocks.get("tools", {})), contact_section(blocks.get("contact", {}), site)]
    sections = "\n\n".join(parts[1:]) + "\n"

    base = site["site_url"].rstrip("/") + "/"
    image = site.get("share_image", "og-image.png")
    image_url = image if image.startswith("http") else base + image
    tpl = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
    values = {
        "title": attr(site.get("page_title", site["name"])),
        "description": attr(site.get("page_description", "")),
        "og_title": attr(site.get("share_title", site["name"])),
        "og_description": attr(site.get("share_description", "")),
        "og_image": attr(image_url),
        "site_url": attr(base),
        "name": esc(site["name"]),
    }
    for k, v in values.items():
        tpl = tpl.replace("{{" + k + "}}", v)
    tpl = tpl.replace("<!--INTRO-->", parts[0]).replace("<!--SECTIONS-->", sections)
    (ROOT / "index.html").write_text(tpl, encoding="utf-8")

    print(f"index.html written ({len(tpl) // 1024} KB), {len(ORDER)} project sections.")
    if "YOUR-" in site["site_url"]:
        print("note: site_url in content.md still has the placeholder. Set it to your real address "
              "so the LinkedIn preview picture works.")


if __name__ == "__main__":
    main()
