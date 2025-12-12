class Snake:

    def __init__(self):
        self.body = [[200,50],[190,50],[180,50],[170,50]]
        self.head = [200,50]#X, Y
        self.tail = [170,50]
        self.direction = "RIGHT"
        self.change_direction = self.direction
        self.alive = True

    def move(self):
        if self.change_direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        elif self.change_direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'

        elif self.change_direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'

        elif self.change_direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'

        if self.direction == 'RIGHT':
            self.head[0] = self.head[0] + 10
            
        elif self.direction == 'LEFT':
            self.head[0] = self.head[0] - 10

        elif self.direction == 'DOWN':
            self.head[1] = self.head[1] + 10

        elif self.direction == 'UP':
            self.head[1] = self.head[1] - 10

        self.body.insert(0, list(self.head))
        self.tail = self.body.pop(-1)

    def add_length(self, collision):
        if collision:
            self.body.append(self.tail)
            
    def hit_wall(self, width, height):
        if self.head[0] < 0 or self.head[0] > width-10:
            self.alive = False
            return True
        
        elif  self.head[1] < 0 or self.head[1] > height-10:
            self.alive = False
            return True
        
    def hit_body(self):
        if self.head in self.body[1:]:
            self.alive = False
            return True

        else:
            return False     