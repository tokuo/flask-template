from config import build_app
from main.service import DemoService

from flask import render_template


app = build_app()

@app.route('/')
def hello():
    DemoService.demo_service()
    demo_attribute = [app.config['TEMPLATE_ENGINE']]
    return render_template('home.html', test_list=demo_attribute)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'])
    app.logger.info("flask app stopped.")
