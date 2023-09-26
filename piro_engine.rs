pub struct PiroEngine {
    games: Vec<Game>,
}

pub struct Game {
    name: String,
    status: GameStatus,
}

pub enum GameStatus {
    Initialized,
    Running,
    Stopped,
}

impl PiroEngine {
    pub fn new() -> PiroEngine {
        PiroEngine { games: Vec::new() }
    }

    pub fn create_game(&mut self, game_name: &str) {
        let new_game = Game {
            name: String::from(game_name),
            status: GameStatus::Initialized,
        };
        self.games.push(new_game);
    }

    pub fn start_game(&mut self, game_name: &str) {
        for game in &mut self.games {
            if game.name == game_name {
                game.status = GameStatus::Running;
            }
        }
    }

    pub fn stop_game(&mut self, game_name: &str) {
        for game in &mut self.games {
            if game.name == game_name {
                game.status = GameStatus::Stopped;
            }
        }
    }

    pub fn list_running_games(&self) -> Vec<String> {
        let mut running_games = Vec::new();
        for game in &self.games {
            if game.status == GameStatus::Running {
                running_games.push(game.name.clone());
            }
        }
        running_games
    }

    pub fn list_initialized_games(&self) -> Vec<String> {
        let mut initialized_games = Vec::new();
        for game in &self.games {
            if game.status == GameStatus::Initialized {
                initialized_games.push(game.name.clone());
            }
        }
        initialized_games
    }
}

fn main() {
    let mut engine = PiroEngine::new();

    engine.create_game("Game1");
    engine.create_game("Game2");

    engine.start_game("Game1");

    let running_games = engine.list_running_games();
    let initialized_games = engine.list_initialized_games();

    println!("Running games: {:?}", running_games);
    println!("Initialized games: {:?}", initialized_games);
}
