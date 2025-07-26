from datetime import datetime
from pathlib import Path

BASE_URL = "https://workkit.kr"
today = datetime.utcnow().strftime("%Y-%m-%d")

def main():
    html_files = sorted(Path(".").glob("*.html"))
    html_files = [f for f in html_files if f.name not in ["index.html", "sitemap.xml"]]

    url_entries = []
    for file in html_files:
        url_entries.append(f"""  <url>
    <loc>{BASE_URL}/{file.name}</loc>
    <lastmod>{today}</lastmod>
  </url>""")

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(url_entries)}
</urlset>"""

    Path("sitemap.xml").write_text(sitemap_content, encoding="utf-8")

if __name__ == "__main__":
    main()
