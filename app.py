from flask import Flask, request, render_template, redirect, url_for

from forms import BookForm
from models import library

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/library/", methods=["GET", "POST"])
def library_list():
    form = BookForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            library.create(form.data)
            library.save_all()
        return redirect(url_for("library_list"))

    return render_template("library.html", form=form, library=library.all(), error=error)


@app.route("/book/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = library.get(book_id - 1)
    form = BookForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            library.update(book_id - 1, form.data)
        return redirect(url_for("library_list"))
    return render_template("book.html", form=form, book_id=book_id)


if __name__ == "__main__":
    app.run(debug=True)