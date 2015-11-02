from flaskapp import create_app

application = create_app(app_config='DEVELOPMENT')

if __name__ == '__main__':
    application.run()
