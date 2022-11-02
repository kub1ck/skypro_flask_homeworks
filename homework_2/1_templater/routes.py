from flask import render_template
from app import app


@app.route('/users/<id>')
def users(id):
    return render_template(
        'users/show.html',
        name=id,
    )


if __name__ == '__main__':
    app.run(debug=True)