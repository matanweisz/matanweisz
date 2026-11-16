# /// script
# requires-python = ">=3.12"
# dependencies = ["pillow"]
# ///
"""Build assets/skills/<category>.svg: icon tiles with a name under each.

Edit SKILLS, then run: uv run tools/skills.py
Icon sources: skillicons.dev (id), simple-icons (si:slug), or a file in assets/logos/ (file:name).
"""
import base64, io, re, urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

SKILLS = {
    "ai": [("vLLM", "file:vllm.png"), ("SGLang", "file:sglang.png"), ("NVIDIA GPUs", "si:nvidia"),
           ("Hugging Face", "si:huggingface"), ("Claude Code", "si:claude"), ("MCP", "si:modelcontextprotocol"),
           ("n8n", "si:n8n")],
    "kubernetes": [("Kubernetes", "kubernetes"), ("Docker", "docker"), ("Helm", "si:helm")],
    "cloud": [("AWS", "aws"), ("Google Cloud", "gcp")],
    "iac": [("Terraform", "terraform"), ("Crossplane", "file:crossplane.svg"), ("SaltStack", "si:saltproject"),
            ("Vagrant", "si:vagrant")],
    "cicd": [("GitHub Actions", "githubactions"), ("GitLab CI", "gitlab"), ("Jenkins", "jenkins"), ("Argo CD", "si:argo")],
    "observability": [("Prometheus", "prometheus"), ("Grafana", "grafana"), ("Loki", "file:loki.png"),
                      ("Mimir", "file:mimir.png"), ("Alloy", "file:alloy.svg")],
    "code": [("Python", "py"), ("Bash", "bash"), ("Go", "go"), ("Linux", "linux"), ("Git", "git"), ("nginx", "nginx")],
    "apps": [("FastAPI", "fastapi"), ("React", "react"), ("TypeScript", "ts"), ("Tailwind", "tailwind"),
             ("Supabase", "supabase"), ("Kafka", "kafka"), ("Redis", "redis"), ("MongoDB", "mongodb"),
             ("PostgreSQL", "postgres")],
}

TILE, PITCH, CAP, ROW = 44, 84, 18, 74  # px: icon size, column width, caption gap, row height
BG = "#242938"  # skillicons' dark tile, so every tile matches


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "profile-builder"})) as r:
        return r.read()


def inner(svg, prefix):
    """Body of an <svg>, with ids prefixed so icons in one file don't clash."""
    body = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S)[1]
    return re.sub(r'(id="|url\(#|href="#)([^")]+)', lambda m: f"{m[1]}{prefix}{m[2]}", body)


def png_uri(path):
    im = Image.open(path).convert("RGBA")
    im.thumbnail((160, 160))
    if path.name == "vllm.png":  # the official file has a white background
        px = im.load()
        for x in range(im.width):
            for y in range(im.height):
                if min(px[x, y][:3]) > 245:
                    px[x, y] = (255, 255, 255, 0)
    buf = io.BytesIO(); im.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


def tile(src, n):
    """One 256-unit tile, like a skillicons icon."""
    if not src.startswith(("si:", "file:")):
        return inner(get(f"https://skillicons.dev/icons?i={src}").decode(), f"i{n}")
    out = f'<rect width="256" height="256" rx="60" fill="{BG}"/>'
    if src.startswith("si:"):
        svg = get(f"https://cdn.simpleicons.org/{src[3:]}").decode()  # official CDN, in the brand colour
        path = re.search(r' d="([^"]+)"', svg)[1]
        color = re.search(r'fill="(#[0-9a-fA-F]{6})"', svg)[1]
        r, g, b = (int(color[i:i + 2], 16) for i in (1, 3, 5))
        if 0.2126 * r + 0.7152 * g + 0.0722 * b < 80:  # dark brand colour on a dark tile: use white
            color = "#FFFFFF"
        return out + f'<g transform="translate(56 56) scale(6)"><path d="{path}" fill="{color}"/></g>'
    f = ROOT / "assets" / "logos" / src[5:]
    uri = png_uri(f) if f.suffix == ".png" else "data:image/svg+xml;base64," + base64.b64encode(f.read_bytes()).decode()
    return out + f'<image href="{uri}" x="40" y="40" width="176" height="176" preserveAspectRatio="xMidYMid meet"/>'


def build(name, items):
    per_row = len(items) if len(items) <= 5 else -(-len(items) // 2)
    rows = -(-len(items) // per_row)
    w, h = per_row * PITCH, rows * ROW
    parts = []
    for n, (label, src) in enumerate(items):
        x = (n % per_row) * PITCH + (PITCH - TILE) / 2
        y = (n // per_row) * ROW
        parts.append(f'<svg x="{x}" y="{y}" width="{TILE}" height="{TILE}" viewBox="0 0 256 256">{tile(src, n)}</svg>'
                     f'<text x="{x + TILE / 2}" y="{y + TILE + CAP}" class="cap">{label}</text>')
    alt = ", ".join(label for label, _ in items)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{alt}">'
           f'<title>{alt}</title><style>.cap{{font:600 11px -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;fill:#57606a;text-anchor:middle}}'
           f'@media (prefers-color-scheme:dark){{.cap{{fill:#adbac7}}}}</style>{"".join(parts)}</svg>\n')
    out = ROOT / "assets" / "skills" / f"{name}.svg"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg)
    print(f"{out.relative_to(ROOT)}: {len(items)} icons, {len(svg) // 1024} KB")


if __name__ == "__main__":
    for name, items in SKILLS.items():
        build(name, items)
