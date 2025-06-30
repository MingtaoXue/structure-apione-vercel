from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return {"message": "API is working"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    user_input = data.get("user_input", "")
    
    # 你可以在此插入你的“薛明涛模型”逻辑
    response = f"已收到请求：{user_input}，正在处理薛明涛结构预测。"
    
    return jsonify({"result": response})
