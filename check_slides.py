from playwright.sync_api import sync_playwright
import os

html_path = os.path.abspath("claude-study/slides.html")
file_url = f"file://{html_path}"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 720})
    page.goto(file_url)
    page.wait_for_load_state('networkidle')

    # 全スライドのスクリーンショットを撮る
    # Reveal.jsのスライド数を取得
    slide_count = page.evaluate("""
        () => {
            if (typeof Reveal !== 'undefined') {
                return Reveal.getTotalSlides();
            }
            return 0;
        }
    """)

    print(f"Total slides: {slide_count}")

    # 各スライドのスクリーンショットを撮る
    for i in range(min(slide_count, 30)):  # 最大30枚まで
        page.evaluate(f"Reveal.slide({i})")
        page.wait_for_timeout(300)

        # 現在のスライド情報を取得
        indices = page.evaluate("() => Reveal.getIndices()")
        h = indices.get('h', 0)
        v = indices.get('v', 0)

        page.screenshot(path=f"slide_{i:02d}_h{h}_v{v}.png")
        print(f"Screenshot: slide_{i:02d}_h{h}_v{v}.png")

        # 次のスライドへ
        page.keyboard.press("ArrowRight")
        page.wait_for_timeout(200)

    browser.close()
