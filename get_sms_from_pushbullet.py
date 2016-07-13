import json
from urllib import request

TOKEN = input('Enter your authentication token: ')
DEVICE_ID = input('Enter your device id: ')


def make_request(last_bit):
    """ Make requests with from template + last_bit of url
    """
    req = request.Request(
        'https://api.pushbullet.com/v2/permanents/' + DEVICE_ID + last_bit,
        headers={'Access-Token': TOKEN}
    )

    # convert byte list to string and read json
    response = request.urlopen(req).read().decode('utf-8')
    return json.loads(response)

# Get the threads list
threads = make_request('_threads')

# Add messages to each thread
for thread in threads["threads"]:
    thread['messages'] = make_request('_thread_' + thread['id'])

# Save threads to file in json
with open('sms_json_save', 'w') as f:
    json.dump(threads, f)
