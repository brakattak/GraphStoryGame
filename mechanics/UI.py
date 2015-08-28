import StoryStructure as SS
import time

class UI:
    def __init__(self,story):
        self.s = story

    def run(self):
        self.print_i('\n'+self.s.outcome())
        time.sleep(2)
        while(self.s.choice()):
            if(self.s.choice()[0]=='user_choice'):
                self.manual_decide()
                self.print_i('\n'+self.s.outcome())
            elif(self.s.choice()[0]=='prob_decide'):
                self.auto_decide()
                self.print_i(self.s.outcome())
        print('')

    def print_i(self,i):
        if(i.strip() != ''):
            print(i)

    def manual_decide(self):
        c = self.s.choice()
        i = raw_input(c[1]+'\n\t').lower()
        self.s.decide(int(c[3][c[2].index(i)]))

    def auto_decide(self):
        c = self.s.choice()
        self.print_i(c[1])
        self.s.prob_decide()
        time.sleep(1.5)

if __name__ == '__main__':
    s = SS.StoryStructure('test.txt')
    ui = UI(s)
    ui.run()
