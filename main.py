from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/nama')
def nama():
    return "halaman nama"

# routing flask dinamis
@app.route('/nama/<string:nama>')
def getnama(nama):
    return "nama anda adalah {}".format(nama)

@app.route('/mahasiswa')
def getmahasiswa():
    kelas = 'IF-4201'
    return render_template('mahasiswa.html', kelas=kelas)

@app.route('/dosen')
def getdosen():
    hobi = ['membaca', 'jalan-jalan', 'nonton']
    return render_template('dosen.html', hobi=hobi)

if __name__ == '__main__':
    app.run(debug=True)
