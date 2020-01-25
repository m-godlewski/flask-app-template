import core, config

if __name__ == '__main__':  
    core.app.debug=config.DEBUG
    core.app.run(host='0.0.0.0', port=config.PORT)