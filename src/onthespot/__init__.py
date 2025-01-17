import os
# Required for librespot-python
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'


if __name__ == '__main__':
    from main import main
    main()
