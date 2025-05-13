#!/usr/bin/env python3
from app import app, HOST, PORT, DEBUG, logger

if __name__ == '__main__':
    logger.info(f"Starting Calculator App on http://{HOST}:{PORT}")
    logger.info(f"Debug mode: {DEBUG}")
    logger.info("Press Ctrl+C to quit")
    app.run(host=HOST, port=PORT, debug=DEBUG)