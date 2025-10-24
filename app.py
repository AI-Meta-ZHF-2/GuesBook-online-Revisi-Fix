from flask import Flask, render_template, request, redirect

app = Flask(__name__)

guest_entries = []

@app.route("/", methods=["GET", "POST"])
def index():
    global guest_entries
    
    if request.method == "POST":
        action = request.form.get("action")
        
        if action == "submit":
            nama = request.form.get("nama")
            kontak = request.form.get("kontak")
            instansi = request.form.get("instansi")
            tujuan = request.form.get("tujuan")
            catatan = request.form.get("catatan")

            if nama and kontak and instansi and tujuan:
                guest_entries.append([nama, kontak, instansi, tujuan, catatan])
        
        elif action == "clear":
            guest_entries = []

        return redirect("/")

    return render_template("index.html", data=guest_entries)

if __name__ == "__main__":
    app.run(debug=True)
