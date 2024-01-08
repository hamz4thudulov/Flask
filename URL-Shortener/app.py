from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory dictionary to store URL mappings
url_mapping = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('long_url')

    # Check if the URL is already shortened
    short_url = next((short for short, url in url_mapping.items() if url == long_url), None)

    # If not, generate a new short URL
    if not short_url:
        short_url = generate_short_url()
        url_mapping[short_url] = long_url

    return render_template('index.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return render_template('not_found.html')

def generate_short_url():
    # This is a simple function to generate a short URL (you might want to use a more robust method)
    return str(len(url_mapping) + 1)

if __name__ == '__main__':
    app.run(debug=True)
