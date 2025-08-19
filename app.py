from header import get_header
from main import get_main
from footer import get_footer

def build_page():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Modular HTML</title>
    </head>
    <body>
        {get_header()}
        {get_main()}
        {get_footer()}
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    page = build_page()
    with open("index.html", "w") as f:
        f.write(page)
    print("✅ index.html created successfully!")
