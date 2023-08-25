from flask import jsonify
from . import v1_bp
from app.models.question import Question

@v1_bp.route("/questions", methods=["GET"])
def get_all_questions():
    questions = Question.get_all()
    return jsonify([questions.to_dict() for question in questions]), 200