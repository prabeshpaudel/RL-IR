import random
import matplotlib.pyplot as plot

a = 0.6
b = 0.4
c = 0.35
class RecyclingRobot:

    def __init__(self):
        self.charge = "high"      # In this case True is high battery and False is low battery 
        self.reward = 0
        self.alpha = 0.5
        # self.foundCanProb = 0.2
        self.beta = 0.5
        self.r_wait = 1
        self.r_search = 2
        self.gamma = 0.5
        self.actions = {"high":["search", "wait"], 
                        "low":["search", "wait", "recharge"]}
        self.action = "search"
        # self.probabilities = {
        #                         ["high", "wait", "high"]: [1, self.r_wait],
        #                         ["high", "wait", "low"] : [0, None], 
        #                         ["high", "search", "high"]: [self.alpha, self.r_search],
        #                         ["high", "search", "low"]: [1- self.alpha, self.r_search],
        #                         ["low", "search", "high"]: [1 - self.beta, -3],
        #                         ["low", "search", "low"]: [self.beta, self.r_search],
        #                         ["low", "wait", "high"]: [0, None],
        #                         ["low", "wait", "low"]: [1, self.r_wait], 
        #                         ["low", "recharge", "high"]: [1, 0],
        #                         ["low", "recharge", "low"]: [0, None]
        #                     }

    # def search(self):
        # if self.charge_level < 50:
        #     self.charge = False           
        # if self.charge <= 0:
        #     self.reward -= 10
        
        # #TODO
        # if random.random() < self.alpha and self.charge == "high":
        #     self.charge = "low"
        #     reward += self.r_search
        # else:

    def prob(self, S, A):
        if S == "high" and A == "search":
            if random.random() < self.alpha:
                print("high ", " search ", " high")
                # print("X")
                self.charge = "high"
                self.reward += self.gamma*self.r_search
            else:
                # print("Y")
                print("high ", " search ", " low")
                self.charge = "low"
                self.reward += self.gamma*self.r_search

        if S == "low" and A == "search":
            if random.random() < self.beta:
                print("low ", " search ", " low")
                self.charge = "low"
                self.reward += self.gamma*self.r_search
            else:
                print("low ", " search ", " high")
                self.charge = "high"
                self.reward -= 3
        
        if S == "high" and A == "wait":
            print("high ", " wait ", " high")
            self.charge = "high"
            self.reward += self.gamma*self.r_wait
            
        if S == "low" and A == "wait":
            print("low ", " wait ", " low")
            self.charge = "low"
            self.reward += self.gamma*self.r_wait

        if S == "low" and A == "recharge":
            print("low ", " recharge ", " high")
            self.charge = "high"
            self.reward += 0


    def step(self):
        #TODO Create a policy funtion that examines the current state and gives an action based on hte probabilities
        
        actions = self.actions[self.charge]
        # currAction = random.sample(actions, 1) # Policy right now is random
        # print(currAction[0], self.charge)
        # self.action = currAction[0]

        # self.action = currAction
        Action_pick = random.random()
        if self.charge== "high":
            if  Action_pick > a:
                self.action = "search"
            else:
                self.action = "wait"
       
        if self.charge == "low":
            if  Action_pick > b:
                self.action = "search"
            elif Action_pick < b and Action_pick < c:
                self.action = "wait"
            else:
                self.action="recharge"
        
        self.prob(self.charge, self.action)
        
    def getState(self):
        return [self.charge, self.action, self.reward]

    # def wait(self, n_cans):
    #     if random.random() < self.foundCanProb:
    #         self.reward += self.r_search

    # def recharge(self):
    #     if not self.charge:
    #         self.charge = 100


def main():
    robot = RecyclingRobot()
    n = 0
    average_reward=[]
    while n < 10000:
        n += 1
        robot.step()
        curr = robot.getState()
        # print(robot.getState())
        # print(curr[0],curr[1],curr[2])
        average_reward.append(curr[2]/n)
    plot.plot(average_reward)
    plot.show()
    # print(robot.getState()[1]/n)
if "__main__" == main():
    main()