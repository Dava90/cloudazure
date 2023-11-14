from openai import OpenAI, AuthenticationError
from flask import Flask, request, render_template, redirect
import os

# Inisialisasi objek OpenAI
openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "kodeapi"))


def fix_bugs(code: str) -> str:
    # kode untuk memperbaiki bug di sini
    response = openai_client.chat.completions.create(
        model="text-davinci-002",  # Ganti dengan model GPT-3 yang sesuai
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": f"##### fix this code\n \n### Buggy Python\n{code}\n    \n### Fixed Python"}],
        temperature=0,
        max_tokens=1000
    )

    fixed_code = response["choices"][0]["message"]["content"]

    return fixed_code

def handle_authentication_error():
    error_message = "Error: Authentication failed. Please check your API key."
    return render_template('tool.html', error_message=error_message)

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk alat perbaikan bug
@app.route('/tool/')
def tool():
    return render_template('tool.html')

# Route untuk halaman about
@app.route('/about/')
def about():
    return render_template('about.html')

# Route untuk halaman kontak
@app.route('/Anggota/')
def contact():
    return render_template('contact.html')

# Route untuk halaman portofolio ketua
@app.route('/ketua_portofolio/')
def ketua_portfolio():
    return render_template('portofolio.html')

# Route untuk halaman portofolio anggota 1
@app.route('/anggota1_portofolio/')
def anggota1_portofolio():
    return render_template('portofolio2.html')

# Route untuk halaman portofolio anggota 2
@app.route('/anggota2_portofolio/')
def anggota2_portofolio():
    return render_template('portofolio3.html')

# Route untuk halaman portofolio anggota 3
@app.route('/anggota3_portofolio/')
def anggota3_portofolio():
    return render_template('portofolio4.html')

# Route untuk menangani permintaan perbaikan bug
@app.route('/fix-bugs/', methods=['POST'])
def fix_bugs_route():
    try:
        buggy_code = request.form['code']
        fixed_code = fix_bugs(buggy_code)
        return render_template('tool.html', fixed_code=fixed_code)
    except AuthenticationError as e:
        return handle_authentication_error()

if __name__ == '__main__':
    app.run()
