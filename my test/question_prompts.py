#這一行引入了自定義的 Question 類，這樣就可以在程式中使用 Question 類。
from Question import Question

#這一段定義了一個列表 question_prompts，
#裡面包含三個問題的提示。提示中包含了選項，用戶可以從中選擇答案。
question_prompts = [
    "足球什麼顏色\n(a) 白色\n(b) 藍色\n(c) 綠色\n(d) 黑色\n",
    "台灣國球是什麼\n(a) 籃球\n(b) 棒球\n(c) 羽毛球\n(d) 高爾夫球\n",
    "棒球經典賽最後一場台灣第幾局得分\n(a) 1局\n(b) 4局\n(c) 7局\n(d) 9局\n", 
    ]

#這一段定義了一個 questions 列表，
#其中包含三個 Question 對象，每個對象代表一個問題和它的正確答案。
#這裡我們使用了 Question 類來創建問題對象，
#並將問題提示和答案作為參數傳遞給類的建構函數。
questions = [
    Question(question_prompts[0], "a"), #這邊是prompts是連結上面的題目 回傳到Question上的 class
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "d")
]

#這一段定義了一個名為 run_test 的函數，它接受一個 questions 參數，
# 即問題列表。函數使用 for 迴圈遍歷 questions 列表中的每個 Question 對象。
# 在每次迭代中，函數顯示問題的提示並等待用戶輸入答案。
# 如果用戶輸入的答案與問題的正確答案匹配，則得分
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt) #用戶的答案回傳
        if answer == question.answer:
            score += 1
        print("You got " + str(score) + "/" + str(len(questions)) + " correct")      

run_test(questions) #這個是把題目的questions 依序列出來
    
        
        
        

        