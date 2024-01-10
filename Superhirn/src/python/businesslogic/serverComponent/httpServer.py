from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        if self.path == '/generate_code':
            response = self.generate_random_code(data['length'], data['max_colour'])
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"code": response}).encode())

        elif self.path == '/generate_feedback':
            response = self.generate_feedback(data['code'], data['guess'])
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"feedback": response}).encode())

    @staticmethod
    def generate_random_code(length, max_colour):
        return ''.join(str(random.randint(1, max_colour)) for _ in range(length))

    @staticmethod
    def generate_feedback(code, guess):
        feedback = ""
        secret_marked = [False] * len(code)
        guess_marked = [False] * len(guess)

        for stone_code_position in range(len(code)):
            if code[stone_code_position] == guess[stone_code_position]:
                feedback += "8"
                secret_marked[stone_code_position] = guess_marked[stone_code_position] = True

        for stone_code_position in range(len(code)):
            if not secret_marked[stone_code_position]:
                for stone_guess_position in range(len(guess)):
                    if (not guess_marked[stone_guess_position]
                            and code[stone_code_position]
                            == guess[stone_guess_position]):
                        feedback += "7"
                        guess_marked[stone_guess_position] = True
                        break

        feedback_list = list(feedback)
        random.shuffle(feedback_list)
        shuffled_feedback = ''.join(feedback_list)
        return shuffled_feedback


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting http server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
