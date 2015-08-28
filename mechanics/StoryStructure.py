import networkx as nx
import read_to_graph as rg
import random

class StoryStructure:
    def __init__(self,filename,cursor=0):
        self.G = rg.read_to_graph(filename,"::")
        self.cursor = cursor
        self.previous = 0

    def outcome(self):
        #throws a Key Error if not exist
        return self.G.edge[self.previous][self.cursor]['text']

    def choice(self):
        if self.G.node[self.cursor]:
            if('choice_text' in self.G.node[self.cursor].keys()):
                return ('user_choice',
                        self.G.node[self.cursor]['text'],
                        self.G.node[self.cursor]['choice_text'],
                        self.G.node[self.cursor]['choice_num'])
            elif('choice_prob' in self.G.node[self.cursor].keys()):
                return ('prob_decide',
                        self.G.node[self.cursor]['text'],
                        self.G.node[self.cursor]['choice_prob'],
                        self.G.node[self.cursor]['choice_num'])
            print('Testing Fail')

    def decide(self,choice):
        self.previous = self.cursor
        self.cursor = choice

    def prob_decide(self):
        choice_num = self.G.node[self.cursor]['choice_num']
        probs = self.G.node[self.cursor]['choice_prob']
        self.previous = self.cursor
        r = random.random()
        sum = 0; count = 0
        for i in probs:
            if(i/100.0+sum > r):
                self.cursor = choice_num[count]
            else:
                sum += i/100.0
                count += 1
    
    def reset_cursor(self,cursor,previous):
        self.cursor = cursor
        self.previous = previous

if __name__ == '__main__':
    s = StoryStructure('test.txt')
    print(s.outcome())
    s.decide(1)
    print(s.outcome())
