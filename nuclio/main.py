#!/usr/bin/env python3
"""
@Filename:    main.py.py
@Author:      dulanj
@Time:        07/12/2021 22:36
"""
import base64
import io
import json

from PIL import Image


def init_context(context):
    context.logger.info('init_context')


def handler(context, event):
    response_body = f'Got {event.method} to {event.path} with "{event.body}"'

    data = event.body
    threshold = data["threshold"]
    buf = io.BytesIO(base64.b64decode(data["image"]))
    image = Image.open(buf)

    # do the prediction

    # log with debug severity
    context.logger.debug(image.size)
    results = []
    results.append({
        "confidence": str(0.8),
        "label": "box",
        "points": [100, 100, 200, 200],
        "type": "rectangle",
    })
    # just return a response instance
    return context.Response(body=json.dumps(results),
                            headers={},
                            content_type='application/json',
                            status_code=201)
