// MultiplayerChat.scala

import scala.collection.mutable

// Define a class to manage the multiplayer chat
class MultiplayerChat {
  private val chatHistory: mutable.Queue[String] = mutable.Queue[String]()

  // Function to send a message to the chat
  def sendMessage(sender: String, message: String): Unit = {
    val formattedMessage = s"[$sender]: $message"
    chatHistory.enqueue(formattedMessage)
    // Notify all connected clients about the new message
    notifyClients(formattedMessage)
  }

  // Function to retrieve the chat history
  def getChatHistory(): Seq[String] = chatHistory.toSeq

  // Function to notify all connected clients about a new message
  private def notifyClients(message: String): Unit = {
    // Implement the logic to broadcast the message to all connected clients here
    // This may involve sending the message over the network to each client
    // For security and optimization, you can use a messaging protocol
  }
}

// Usage example:
val chat = new MultiplayerChat()

// User 1 sends a message
chat.sendMessage("User1", "Hello, everyone!")

// User 2 sends a message
chat.sendMessage("User2", "Hi there!")

// Get the chat history
val chatHistory = chat.getChatHistory()
println("Chat History:")
chatHistory.foreach(println)
