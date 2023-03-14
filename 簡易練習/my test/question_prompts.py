from Question import Question
question_prompts = [
    "足球什麼顏色\n(a) 白色\n(b) 藍色\n(c) 綠色\n(d) 黑色\n\n",
    "台灣國球是什麼\n(a) 籃球\n(b) 棒球\n(c) 羽毛球\n(d) 高爾夫球\n\n",
    "棒球經典賽最後一場台灣第幾局得分\n(a) 1局\n(b) 4局\n(c) 7局\n(d) 9局\n\n", 
    ]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "d")
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
        
run_test(questions)        
        
        
        
        #未完成 需重新讀過 加註解
        