#!/usr/bin/env python3
"""
build.py — Reads config.yaml and updates index.html with your real info.

Usage:
    1. Fill in config.yaml with your links, photo path, etc.
    2. Run: python3 build.py
    3. Open index.html to verify, then push to GitHub!
"""

import re
import sys
from pathlib import Path

def parse_config(config_path: str) -> dict:
    """Parse the simple YAML-like config file into a dict."""
    config = {}
    path = Path(config_path)
    if not path.exists():
        print(f"❌ Config file not found: {config_path}")
        sys.exit(1)

    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            config[key.strip()] = value.strip()
    return config


def update_html(html: str, config: dict) -> str:
    """Apply config values to the HTML template."""

    # --- Profile photo ---
    photo = config.get("profile_photo", "assets/profile-placeholder.svg")
    if photo and photo != "assets/profile-placeholder.svg":
        html = html.replace(
            'src="assets/profile-placeholder.svg"',
            f'src="{photo}"'
        )
        print(f"  ✅ Profile photo → {photo}")
    else:
        print(f"  ⏭️  Profile photo — still using placeholder")

    # --- Email ---
    email = config.get("email", "")
    if email and "TODO" not in email:
        html = html.replace(
            'href="mailto:#"',
            f'href="mailto:{email}"'
        )
        print(f"  ✅ Email → {email}")
    else:
        print(f"  ⏭️  Email — still TODO")

    # --- GitHub ---
    github = config.get("github", "")
    if github and "TODO" not in github:
        html = re.sub(
            r'<a href="#" class="social-link" aria-label="GitHub"',
            f'<a href="{github}" class="social-link" aria-label="GitHub"',
            html
        )
        print(f"  ✅ GitHub → {github}")
    else:
        print(f"  ⏭️  GitHub — still TODO")

    # --- LinkedIn ---
    linkedin = config.get("linkedin", "")
    if linkedin and "TODO" not in linkedin:
        html = re.sub(
            r'<a href="#" class="social-link" aria-label="LinkedIn"',
            f'<a href="{linkedin}" class="social-link" aria-label="LinkedIn"',
            html
        )
        print(f"  ✅ LinkedIn → {linkedin}")
    else:
        print(f"  ⏭️  LinkedIn — still TODO")

    # --- X / Twitter ---
    x_twitter = config.get("x_twitter", "")
    if x_twitter and "TODO" not in x_twitter:
        html = re.sub(
            r'<a href="#" class="social-link" aria-label="X \(Twitter\)"',
            f'<a href="{x_twitter}" class="social-link" aria-label="X (Twitter)"',
            html
        )
        print(f"  ✅ X (Twitter) → {x_twitter}")
    else:
        print(f"  ⏭️  X (Twitter) — still TODO")

    # --- Google Scholar (add icon if URL provided) ---
    scholar = config.get("google_scholar", "")
    if scholar and "TODO" not in scholar:
        # Insert Google Scholar link after the X/Twitter link
        scholar_link = (
            f'\n        <!-- Google Scholar -->\n'
            f'        <a href="{scholar}" class="social-link" aria-label="Google Scholar" title="Google Scholar" target="_blank" rel="noopener">\n'
            f'          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M5.242 13.769L0 9.5 12 0l12 9.5-5.242 4.269C17.548 11.249 14.978 9.5 12 9.5c-2.977 0-5.548 1.748-6.758 4.269zM12 10a7 7 0 1 0 0 14 7 7 0 0 0 0-14z"/></svg>\n'
            f'        </a>'
        )
        # Add after the X/Twitter link block
        html = html.replace(
            '</nav>\n\n      <!-- Navigation -->',
            f'{scholar_link}\n      </nav>\n\n      <!-- Navigation -->'
        )
        print(f"  ✅ Google Scholar → {scholar}")
    else:
        print(f"  ⏭️  Google Scholar — still TODO")

    # --- PhysCaP paper URL ---
    paper_url = config.get("physcap_paper_url", "")
    if paper_url and "TODO" not in paper_url:
        # Add a "Paper" link before the "Project Page" link
        paper_link = (
            f'<a href="{paper_url}" class="pub-link" target="_blank" rel="noopener">\n'
            f'              <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M5 4h14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zm0 2v12h14V6H5zm2 2h10v2H7V8zm0 4h10v2H7v-2zm0 4h7v2H7v-2z"/></svg>\n'
            f'              Paper\n'
            f'            </a>\n            '
        )
        html = html.replace(
            '<a href="https://physcap.github.io/" class="pub-link"',
            f'{paper_link}<a href="https://physcap.github.io/" class="pub-link"'
        )
        print(f"  ✅ PhysCaP paper URL → {paper_url}")
    else:
        print(f"  ⏭️  PhysCaP paper URL — still TODO")

    # --- PhysCaP thumbnail ---
    thumbnail = config.get("physcap_thumbnail", "")
    if thumbnail and "TODO" not in thumbnail:
        # Check if thumbnail file exists
        if Path(thumbnail).exists():
            print(f"  ✅ PhysCaP thumbnail → {thumbnail} (file found)")
        else:
            print(f"  ⚠️  PhysCaP thumbnail → {thumbnail} (file NOT found, skipping)")
    else:
        print(f"  ⏭️  PhysCaP thumbnail — still TODO")

    # --- Lab URL ---
    lab_url = config.get("lab_url", "")
    if lab_url and "TODO" not in lab_url:
        print(f"  ✅ Lab URL → {lab_url} (already set)")

    # --- Advisor URL ---
    advisor_url = config.get("advisor_url", "")
    if advisor_url and "TODO" not in advisor_url:
        html = html.replace(
            'Prof.&nbsp;Shao-Hua Sun',
            f'<a href="{advisor_url}" target="_blank" rel="noopener">Prof.&nbsp;Shao-Hua Sun</a>'
        )
        print(f"  ✅ Advisor URL → {advisor_url}")
    else:
        print(f"  ⏭️  Advisor URL — still TODO")

    return html


def main():
    print("\n🔧 Building website from config.yaml...\n")

    config = parse_config("config.yaml")
    html_path = Path("index.html")

    if not html_path.exists():
        print("❌ index.html not found! Run this from the project root.")
        sys.exit(1)

    html = html_path.read_text()
    updated_html = update_html(html, config)
    html_path.write_text(updated_html)

    # Summary
    todo_count = sum(1 for v in config.values() if "TODO" in v)
    done_count = sum(1 for v in config.values() if v and "TODO" not in v)

    print(f"\n{'─' * 40}")
    print(f"  Done: {done_count} items configured")
    print(f"  Remaining: {todo_count} items still TODO")
    print(f"{'─' * 40}")

    if todo_count > 0:
        print("\n💡 Fill in the remaining TODOs in config.yaml, then run this script again.\n")
    else:
        print("\n🎉 All set! Push to GitHub to deploy.\n")


if __name__ == "__main__":
    main()
