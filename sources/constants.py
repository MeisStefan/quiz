from quiz_question import *
QUIZ_PAGE_START_FONT = "Arial 25"
QUIZ_PAGE_TITLE_FONT = "Arial 20"
QUIZ_PAGE_TITLE = "In cate zile se sarbatoreste Craciunul?"
QUIZ_PAGE_ANSWERS_FONT = "Arial 15"
QUIZ_PAGE_ANSWERS_TITLES = ["3", "1", "4", "2"]
QUIZ_PAGE_START_TEXT = "Christmas Quiz"
QUIZ_PAGE_START_BUTTON = "Start"
QUIZ_QUESTIONS =[QuizQuestion("In cate zile se sarbatoreste Craciunul?", ["3", "1", "4", "2"], "3", 1),
                 QuizQuestion("Care sunt culorile Craciunului?",["rosu, verde, alb", "rosu, galben, albastru", "rosu, verde", "rosu, argintiu"], "rosu, verde",  3),
                 QuizQuestion("Ce culori aveau hainele lui Mos Craciun initial?", ["Albastre", "Portocalii", "Rosii", "Verzi"], "Albastre",  1),
                 QuizQuestion("Unde locuieste Mos Craciun?", ["Peste tot", "La Polul Nord", "In New York", "In Laponia, Finlanda"], "In Laponia, Finlanda", 4),
                 QuizQuestion("Ce se sarbatoreste in a 3-a zi de Craciun?", ["Ajunul Craciunului", "Sfantul Stefan", "Craciunul", "Mos Nicolae"], "Sfantul Stefan", 2),
                 QuizQuestion("In ce tara/tari se sarbatoreste Craciunul?", ["Romania", "In tarile musulmane", "China", "In tarile crestine"], "In tarile crestine", 4),
                 QuizQuestion("Care este cea mai faimoasă bomboană în perioada Crăciunului?", ["Mints", "Ouă de ciocolată", "Turta-dulce", "Bastoane de zahar"], "Bastoane de zahar",  4),
                 QuizQuestion("Care dintre următoarele NU este un cântec de Crăciun?", ["Frosty the Snowman", "Twelve Days of Christmas", "Five Little Turkeys", "Jingle Bells"], "Five Little Turkeys", 3),
                 QuizQuestion("Moș Crăciun a fost inspirat de care persoană reală?", ["Iisus", "Sfantul Nicolae", "Sfântul Francisc", "Dumnezeu"], "Sfantul Nicolae", 2),
                 QuizQuestion("Ce simbolizează culoarea roșie în Crăciun?", ["Sangele lui Iisus", "Dragoste", "Coca-Cola", "Pericol"], "Sangele lui Iisus", 1)]
QUESTIONS_FILE = "quiz_questions.json"