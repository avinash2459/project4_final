from flask import current_app as app, render_template, make_response


@app.errorhandler(404)
def not_found(e):
    """Page not found."""
    return make_response(
        render_template("404.html"),
        404
    )


@app.errorhandler(400)
def bad_request(e):
    """Bad request."""
    return make_response(
        render_template("400.html"),
        400
    )


@app.errorhandler(500)
def server_error(e):
    """Internal server error."""
    return make_response(
        render_template("500.html"),
        500
    )
