using System;
using System.Collections.Generic;

public class ServerFunctions
{
    private Dictionary<int, Player> connectedPlayers;

    public ServerFunctions()
    {
        connectedPlayers = new Dictionary<int, Player>();
    }

    public void ConnectPlayer(int playerId, string playerName)
    {
        Player newPlayer = new Player(playerId, playerName);
        connectedPlayers[playerId] = newPlayer;
        Console.WriteLine($"Player {playerName} connected with ID {playerId}");
    }

    public void DisconnectPlayer(int playerId)
    {
        if (connectedPlayers.ContainsKey(playerId))
        {
            string playerName = connectedPlayers[playerId].Name;
            connectedPlayers.Remove(playerId);
            Console.WriteLine($"Player {playerName} with ID {playerId} disconnected");
        }
        else
        {
            Console.WriteLine($"Player with ID {playerId} is not connected");
        }
    }

    public void SendGameUpdate(int playerId, string update)
    {
        if (connectedPlayers.ContainsKey(playerId))
        {
            string playerName = connectedPlayers[playerId].Name;
            Console.WriteLine($"Sending game update to player {playerName} with ID {playerId}: {update}");
        }
        else
        {
            Console.WriteLine($"Player with ID {playerId} is not connected");
        }
    }
}

public class Player
{
    public int Id { get; private set; }
    public string Name { get; private set; }

    public Player(int id, string name)
    {
        Id = id;
        Name = name;
    }
}
