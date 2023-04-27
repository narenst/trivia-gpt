import openai


class OpenAIService:
    
    @staticmethod
    def get_quiz_question(difficulty: int):
        """
        Use ChatGPT and get a question.
        """
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_quiz_prompt(difficulty=difficulty),
            temperature=0.6,
            max_tokens=512,
        )
        question_text = response.choices[0].text
        json_response = eval(question_text)
        return json_response


    @staticmethod
    def init(app):
        openai.api_key = app.config['OPENAI_API_KEY']


def generate_quiz_prompt(difficulty: int = 1):
    """
    Create ChatGPT prompt for a quiz question based on difficulty
    """
    return f"""
You are now the host of a trivia show. 
Ask a trivia question and give me 4 choices with one of them being the right answer. 
On a difficulty scale of 1 to 10, the question must be a {difficulty}.
Also include the answer in the response. Your response should be in json.
    """