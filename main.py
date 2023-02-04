import os
from app.main import create_app

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.app_context().push()


def run():
    app.run(host='0.0.0.0',port='5000')

if __name__ == '__main__':
    run()
