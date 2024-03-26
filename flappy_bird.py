import pyxel
import random
import NeuralNetwork as nn

TOTAL = 250

class Bird:
    def __init__(self, brain):
        self.y = pyxel.height/2
        self.x = 25
        self.gravity = 0.6
        self.lift = -10
        self.velocity = 0

        self.score = 0
        self.fitness = 0
        #if a brain is passed in then clone it with that brain
        #mutate it or if no brain is passed in like when at init
        #then create new nn
        if isinstance(brain, nn.NeuralNetwork):
            self.nn = brain.copy()
            self.nn.mutate(0.3)
        else:
            self.nn = nn.NeuralNetwork(5,8,1)
            self.nn.mutate(0.3)

    def copy(self):
        #print("copied")
        return Bird(self.nn)
        
    def show(self):
        pyxel.circ(self.x, self.y, 3, 8)

    def update(self):
        ###the longer the bird is alive the higher its score
        self.score+=1
        self.velocity += self.gravity
        self.velocity *= 0.9
        self.y += self.velocity

        if self.y > pyxel.height:
            self.y = pyxel.height
            self.velocity = 0

        if self.y < 0:
            self.y = 0
            self.velocity = 0

        #if pyxel.btnp(pyxel.KEY_SPACE):
        #    self.bird.up()


    def up(self):
        self.velocity += self.lift

    def think(self, pipes):
        #pipe detection algo to find the closest pipe
        if not pipes:
            return
        closest = None
        closestD = 1000000
        for i in range(len(pipes)):
            d = (pipes[i].x + pipes[i].w) - self.x
            if d < closestD and d > 0:
                closest = pipes[i]
                closestD = d
        #take in inputs that are its y pos
        # top, bottom, x
        # bird velocity, 
        # all vals normalized, 
        inputs = []
        inputs.append(self.y / pyxel.height)
        inputs.append(closest.top / pyxel.height)
        inputs.append(closest.bottom / pyxel.height)
        inputs.append(closest.x / pyxel.width)
        inputs.append(self.velocity / 10)
        # if output less than 0.5 dont jump or else jump
        output = self.nn.predict(inputs)
        if output[0] > 0.5:
            self.up()

class Pipe:
    def __init__(self):
        self.spacing = 80
        self.top = random.randrange(pyxel.height / 6, (3/4) * pyxel.height)
        self.bottom = pyxel.height - (self.top + self.spacing)
        self.x = pyxel.width
        self.w = 20
        self.speed = 2
        self.highlight = False

    def hits(self, bird):
        if bird.y < self.top or bird.y > pyxel.height - self.bottom:
            if bird.x > self.x and bird.x < self.x + self.w:
                self.highlight = True
                return True
        self.highlight = False
        return False

    def offscreen(self):
        if self.x < -self.w:
            return True
        else:
            return False

    def show(self):
        col = 7
        if self.highlight:
            col = 8
        pyxel.rect(self.x, 0, self.w, self.top, col)
        pyxel.rect(self.x, pyxel.height - self.bottom, self.w, self.bottom, col)

class App():


    ##this is a genetic algorithm designed for neuroevolution
    def nextGeneration(self):
        ##########CALCULATE THE FITNESS FOR EACH BIRD##########
        self.calculateFitness()
        ######GOING THROUGH ALL SAVED BIRDS FROM PREV GEN AND PICKING ONE???
        ########TO RETURN A NEW BIRD THAT IS A CLONE. HAS ITS BRAIN OR NN
        for i in range(TOTAL):
            self.birds.append(self.pickOne())
        self.savedBirds = []


    def pickOne(self):
        #print("picking one")
        index = 0
        r = random.uniform(0, 1)  # Use random.uniform instead of random.randrange
        while r > 0:
            r -= self.savedBirds[index].fitness
            index += 1  # Increment the index instead of decrementing
        index -= 1  # Decrement the index by 1 after exiting the loop
        bird = self.savedBirds[index]
        child = bird.copy()
        return child


    def calculateFitness(self):
        ############33FOR ALLL BIRDS SUM UP FOR HOW LONG THEY HAVE LIVED AND 
        #######BIRD LIFE TIME / ALL BIRDS LIFE TIME##############
        sum = 0
        for bird in self.savedBirds:
            sum += bird.score
            bird.fitness = bird.score / sum






    def __init__(self):
        pyxel.init(200, 300)
        self.birds = []
        self.savedBirds = []
        self.pipes = []
        global COUNTER
        COUNTER = 0
        ##creating the birds with new brain
        #########INITIALIZING POPULATION###########
        for i in range(TOTAL):
            self.birds.append(Bird(False))
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        ####the point of the counter is to reset the pipes after each gen dies
        global COUNTER
        pyxel.cls(0)
    
        if COUNTER % 80 == 0:
            self.pipes.append(Pipe())
        COUNTER+=1
        #for all the birds they think, update and show
        for bird in self.birds:
            bird.think(self.pipes)
            bird.update()
            bird.show()

        ###for all pipes they update and show
        for i in range(len(self.pipes)-1, -1, -1):
            self.pipes[i].show()
            self.pipes[i].x -= self.pipes[i].speed
            if self.pipes[i].offscreen():
                self.pipes.remove(self.pipes[i])

            for j in range(len(self.birds)-1, -1, -1):
                if self.pipes[i].hits(self.birds[j]):
                    #this might be array of arrays dont want that
                    ###########saving the previous generation#########
                    self.savedBirds.append(self.birds[j])

                    self.birds.remove(self.birds[j])

        if len(self.birds) == 0:
            #######ALL DIED SO CREATING NEW GENERATION#########
            ####DOESNT WORK?????####
            self.nextGeneration()
            self.pipes = []
            #########resetting the pipes
            COUNTER = 0


App()
