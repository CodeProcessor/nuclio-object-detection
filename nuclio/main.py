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
from box.box_detection import BoxDetection


def init_context(context):
    model_file_path = 'box/best_640.torchscript.pt'
    model = BoxDetection(model_file_path)
    context.user_data.model = model
    context.logger.info('init_context')


def handler(context, event):
    response_body = f'Got {event.method} to {event.path} with "{event.body}"'

    data = event.body
    threshold = data["threshold"]
    buf = io.BytesIO(base64.b64decode(data["image"]))
    image = Image.open(buf)

    # log with debug severity
    context.logger.debug(image.size)

    # do the prediction
    results = context.user_data.model.get_boxes(image, threshold)

    # just return a response instance
    return context.Response(body=json.dumps(results),
                            headers={},
                            content_type='application/json',
                            status_code=201)
