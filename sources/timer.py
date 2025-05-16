
from constants import *

class QuizTimer:
    def __init__(self):
        self.timer_ID = None
        self.timeout = QUIZ_TIMEOUT

    def store_timer(self, timer):
        self.timer = timer

    def get_timer(self):
        return self.timer

    def get_current_timer_seconds(self):
        return self.current_timer_seconds

    def decrement_current_timer_seconds(self):
        self.current_timer_seconds -= 1

    def reset_timer(self):
        self.current_timer_seconds = 15
        self.timer.config(text=self.current_timer_seconds)

    def get_timer_ID(self):
        return self.timer_ID

    def store_timer_ID(self, ID):
        self.timer_ID = ID

    def cancel_timer(self):
        self.timer.after_cancel(self.timer_ID)

    def hide_timer(self):
        self.timer.config(text = "")

    def store_next_question_timer_ID(self, ID):
        self.next_question_timer_ID = ID

    def stop_next_question_timer(self):
        self.timer.after_cancel(self.next_question_timer_ID)

quiz_timer = QuizTimer()