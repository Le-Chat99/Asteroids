from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position+= self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20,50)
        angpl = self.velocity.rotate(angle)
        angne = self.velocity.rotate(-angle)
        
        newRad = self.radius-ASTEROID_MIN_RADIUS
        newApl = Asteroid(self.position.x, self.position.y,newRad)
        newAne = Asteroid(self.position.x, self.position.y,newRad)
        
        newApl.velocity=angpl*1.2
        newAne.velocity=angne*1.2