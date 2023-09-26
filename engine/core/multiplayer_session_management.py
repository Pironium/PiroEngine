# Import necessary modules
import random
import time

# Define a class for managing multiplayer game sessions
class MultiplayerSessionManager:
    def __init__(self):
        self.sessions = {}  # Dictionary to store active game sessions

    def create_session(self, game_id, max_players):
        # Generate a unique session ID
        session_id = f"{game_id}_{random.randint(1000, 9999)}"

        # Create a new game session
        session = {
            "session_id": session_id,
            "game_id": game_id,
            "max_players": max_players,
            "players": [],
            "created_at": time.time(),
        }

        # Add the session to the dictionary
        self.sessions[session_id] = session
        return session_id

    def join_session(self, session_id, player_id):
        # Check if the session exists
        if session_id in self.sessions:
            session = self.sessions[session_id]

            # Check if the session is not full
            if len(session["players"]) < session["max_players"]:
                # Add the player to the session
                session["players"].append(player_id)
                return True
            else:
                return False  # Session is full
        else:
            return False  # Session does not exist

    def leave_session(self, session_id, player_id):
        # Check if the session exists
        if session_id in self.sessions:
            session = self.sessions[session_id]

            # Check if the player is in the session
            if player_id in session["players"]:
                # Remove the player from the session
                session["players"].remove(player_id)
                return True
            else:
                return False  # Player is not in the session
        else:
            return False  # Session does not exist

    def list_sessions(self):
        # Return a list of active sessions
        return list(self.sessions.values())
