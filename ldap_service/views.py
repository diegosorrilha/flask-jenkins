from flask import Flask, render_template, request

from services import get_lineup_id_by_account_number


def init_app(app: Flask):

    @app.route('/get-lineupid', methods=['GET', 'POST'])
    def get_lineupid():
        lineup_id = None
        error = False

        if request.method == 'POST':
            account_number = request.form.get('account_number')
            lineup_id = get_lineup_id_by_account_number(account_number)

            if not lineup_id:
                error = True

        return render_template('get_lineupid.html', lineup_id=lineup_id, error=error)
