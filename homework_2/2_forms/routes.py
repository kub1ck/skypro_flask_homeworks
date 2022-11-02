from flask import render_template, request
from app import app, users


@app.route('/users')
def index():
    key = request.args.get('key') if request.args.get('key') else ''
    filtered_courses = filter(lambda user: key in user, users)

    return render_template(
        'index.html',
        users=filtered_courses,
        search=key
    )


app.run(debug=True)
