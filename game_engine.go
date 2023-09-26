package main

import "fmt"

type PiroEngine struct {
    games map[string]string
}

func NewPiroEngine() *PiroEngine {
    return &PiroEngine{
        games: make(map[string]string),
    }
}

func (engine *PiroEngine) CreateGame(gameName string) {
    engine.games[gameName] = "initialized"
}

func (engine *PiroEngine) StartGame(gameName string) {
    if status, exists := engine.games[gameName]; exists {
        if status == "initialized" {
            engine.games[gameName] = "running"
        }
    }
}

func (engine *PiroEngine) StopGame(gameName string) {
    if status, exists := engine.games[gameName]; exists {
        if status == "running" {
            engine.games[gameName] = "stopped"
        }
    }
}

func (engine *PiroEngine) ListRunningGames() []string {
    runningGames := []string{}
    for gameName, status := range engine.games {
        if status == "running" {
            runningGames = append(runningGames, gameName)
        }
    }
    return runningGames
}

func (engine *PiroEngine) ListInitializedGames() []string {
    initializedGames := []string{}
    for gameName, status := range engine.games {
        if status == "initialized" {
            initializedGames = append(initializedGames, gameName)
        }
    }
    return initializedGames
}

func main() {
    engine := NewPiroEngine()
    engine.CreateGame("Game1")
    engine.StartGame("Game1")

    runningGames := engine.ListRunningGames()
    initializedGames := engine.ListInitializedGames()

    fmt.Println("Running Games:", runningGames)
    fmt.Println("Initialized Games:", initializedGames)
}
