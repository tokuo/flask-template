import os
import logging
from flask import Flask

class DevConfig:
    LOG_LEVEL = logging.INFO
    PORT = 5000
    TEMPLATE_ENGINE = 'Jinja2'

class ProdConfig:
    LOG_LEVEL = logging.INFO
    PORT = 5000
    TEMPLATE_ENGINE = 'Jinja2'

config_selector = {
    'default': DevConfig,
    'dev': DevConfig,
    'prod': ProdConfig
}

# 各モジュールにて、既に以下メソッドで生成されたapp.configを利用するにはcurrent_app.configを利用する（推奨）
# もしくは再度appを生成する（非推奨）
def build_app():
    app = Flask(__name__)
    config_env = os.getenv('FLASK_CONFIG', 'default')
    app.logger.setLevel(config_selector[config_env].LOG_LEVEL)
    app.config.from_object(config_selector[config_env])
    return app
