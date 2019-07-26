from main.demo import DemoHoge, DemoFuga

from flask import current_app


def demo_service():
    current_app.logger.info("message: %s", "demo_log_message")
    DemoHoge.demo_hoge()
    DemoFuga.demo_fuga()
