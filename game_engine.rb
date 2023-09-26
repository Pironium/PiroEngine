class PiroEngine
  def initialize
    @games = {}
  end

  def create_game(game_name)
    @games[game_name] = 'initialized'
  end

  def start_game(game_name)
    if @games[game_name] == 'initialized'
      @games[game_name] = 'running'
    end
  end

  def stop_game(game_name)
    if @games[game_name] == 'running'
      @games[game_name] = 'stopped'
    end
  end

  def list_running_games
    @games.select { |_, status| status == 'running' }.keys
  end

  def list_initialized_games
    @games.select { |_, status| status == 'initialized' }.keys
  end
end

# Пример использования PiroEngine
engine = PiroEngine.new
engine.create_game('Game1')
engine.start_game('Game1')

running_games = engine.list_running_games
initialized_games = engine.list_initialized_games

puts 'Running Games:', running_games
puts 'Initialized Games:', initialized_games
