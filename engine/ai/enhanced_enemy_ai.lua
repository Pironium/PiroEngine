-- Enhanced Enemy AI for PiroEngine
-- This code implements advanced enemy behavior using Lua

-- Define a class for enhanced enemy AI
EnhancedEnemyAI = {}
EnhancedEnemyAI.__index = EnhancedEnemyAI

function EnhancedEnemyAI.new()
    local self = setmetatable({}, EnhancedEnemyAI)
    self.target = nil
    self.path = {}
    self.currentNode = 1
    self.sightRange = 1000
    self.attackRange = 200
    return self
end

function EnhancedEnemyAI:calculatePathToTarget()
    -- Implement pathfinding algorithm here
    -- This code generates a path to the player's location
    self.path = Pathfinding.calculatePath(self.gameObject.position, self.target.position)
end

function EnhancedEnemyAI:update()
    -- Check if the player is in sight range
    if self.target and Vector3.distance(self.gameObject.position, self.target.position) <= self.sightRange then
        self:calculatePathToTarget()

        -- Follow the calculated path
        if self.currentNode <= #self.path then
            local nextNode = self.path[self.currentNode]
            local direction = nextNode - self.gameObject.position
            direction:normalize()
            self.gameObject:move(direction * self.gameObject.speed)
            
            -- Check if the player is in attack range
            if Vector3.distance(self.gameObject.position, self.target.position) <= self.attackRange then
                self:attackPlayer()
            end
        end
    else
        -- Player is not in sight range, so idle or patrol behavior
        self:idleOrPatrol()
    end
end

function EnhancedEnemyAI:attackPlayer()
    -- Implement advanced attack behavior here
    -- This code handles enemy attacks on the player
    self.gameObject:shoot()
end

function EnhancedEnemyAI:idleOrPatrol()
    -- Implement idle or patrol behavior here
    -- This code defines what the enemy does when the player is not in sight
    self.gameObject:patrol()
end

return EnhancedEnemyAI
