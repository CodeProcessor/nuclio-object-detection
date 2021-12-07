#!/usr/bin/env python3
"""
@Filename:    main.py.py
@Author:      dulanj
@Time:        07/12/2021 22:36
"""


def handler(context, event):
    response_body = f'Got {event.method} to {event.path} with "{event.body}"'

    # log with debug severity
    context.logger.debug('This is a debug level message')

    # just return a response instance
    return context.Response(body=response_body,
                            headers=None,
                            content_type='text/plain',
                            status_code=201)
