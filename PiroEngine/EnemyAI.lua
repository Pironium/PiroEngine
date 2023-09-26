-- PiroEngine Enemy AI Module

-- Define the enemy class
local Enemy = {}
Enemy.__index = Enemy

-- Constructor for the Enemy class
function Enemy.new()
    local self = setmetatable({}, Enemy)
    self.health = 100
    self.position = {x = 0, y = 0, z = 0}
    self.target = nil
    self.speed = 5
    return self
end

-- Method to set the target for the enemy
function Enemy:setTarget(target)
    self.target = target
end

-- Method to update the enemy's position based on AI logic
function Enemy:update()
    if self.target then
        -- Calculate direction to the target
        local direction = {
            x = self.target.position.x - self.position.x,
            y = self.target.position.y - self.position.y,
            z = self.target.position.z - self.position.z
        }
        
        -- Normalize direction vector
        local length = math.sqrt(direction.x^2 + direction.y^2 + direction.z^2)
        direction.x = direction.x / length
        direction.y = direction.y / length
        direction.z = direction.z / length
        
        -- Move the enemy towards the target
        self.position.x = self.position.x + direction.x * self.speed
        self.position.y = self.position.y + direction.y * self.speed
        self.position.z = self.position.z + direction.z * self.speed
    end
end

-- Method to check if the enemy is dead
function Enemy:isDead()
    return self.health <= 0
end

-- Export the Enemy class
return Enemy
