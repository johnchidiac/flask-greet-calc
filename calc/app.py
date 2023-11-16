from flask import Flask, request
import operations

app = Flask(__name__)


@app.route("/<fn>")
@app.route("/math/<fn>")
def return_result(fn):
    
    """Return the result of the math operation"""

    function_to_call = getattr(operations, fn, None)
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    if function_to_call:
        result = function_to_call(a, b)
        return str(result)
    else:
        return "Function not found", 404

