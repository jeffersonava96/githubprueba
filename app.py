from flask import Flask, request, jsonify, render_template_string
import re

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template_string('''
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Calculadora Web</title></head>
<body>
  <input id="display" style="width:200px;font-size:20px;text-align:right" readonly>
  <div>
    <button onclick="press('7')">7</button><button onclick="press('8')">8</button><button onclick="press('9')">9</button><button onclick="press('/')">/</button><br>
    <button onclick="press('4')">4</button><button onclick="press('5')">5</button><button onclick="press('6')">6</button><button onclick="press('*')">*</button><br>
    <button onclick="press('1')">1</button><button onclick="press('2')">2</button><button onclick="press('3')">3</button><button onclick="press('-')">-</button><br>
    <button onclick="press('0')">0</button><button onclick="press('.')">.</button><button onclick="equals()">=</button><button onclick="press('+')">+</button><br>
    <button onclick="clearDisplay()">C</button>
  </div>
  <script>
    function press(v){document.getElementById('display').value += v}
    function clearDisplay(){document.getElementById('display').value = ''}
    async function equals(){
      const expr = document.getElementById('display').value;
      const res = await fetch('/eval',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({expr})});
      const j = await res.json();
      document.getElementById('display').value = j.result;
    }
  </script>
</body>
</html>
''')

    @app.route('/eval', methods=['POST'])
    def evaluate():
        data = request.get_json() or {}
        expr = data.get('expr','')
        if not re.fullmatch(r'[0-9+\-*/. ]+', expr):
            return jsonify(result='Error')
        try:
            # safe-ish eval: only numbers and operators allowed by regex
            result = eval(expr)
        except Exception:
            return jsonify(result='Error')
        return jsonify(result=str(result))

    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000)
