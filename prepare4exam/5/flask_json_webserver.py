import argparse
from json import load, dumps
from flask import Flask, request

app = Flask(__name__)


@app.route('/offense')
def offense():
    with open(filename) as json_file:
        selected_rules = []
        rules = load(json_file)
        for rule in rules:
            if rule['punishment'] == rule_type:
                selected_rules.append(rule)
        return dumps(selected_rules)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--address")
    parser.add_argument("--port")
    parser.add_argument("--filename")
    parser.add_argument("--type")

    args = parser.parse_args()

    filename = args.filename
    rule_type = args.type

    app.run(port=args.port, host=args.address)
