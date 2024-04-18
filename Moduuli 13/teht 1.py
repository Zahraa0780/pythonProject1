from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/alkuluku/<int:num>', methods=['GET'])
def check_prime(num):
    prime = is_prime(num)
    response = {"Number": num, "isPrime": prime}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
