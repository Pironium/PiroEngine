import Foundation

// Define a struct for representing advertisements
struct Advertisement {
    var title: String
    var content: String
    var imageURL: URL
}

// Create a class for managing advertisements
class AdvertisingManager {
    private var ads: [Advertisement] = []
    
    // Function to add an advertisement
    func addAdvertisement(title: String, content: String, imageURL: URL) {
        let newAd = Advertisement(title: title, content: content, imageURL: imageURL)
        ads.append(newAd)
    }
    
    // Function to display an advertisement
    func displayAdvertisement() -> Advertisement? {
        guard let randomAd = ads.randomElement() else {
            return nil
        }
        
        // Simulate displaying the advertisement
        print("Displaying Advertisement:")
        print("Title: \(randomAd.title)")
        print("Content: \(randomAd.content)")
        print("Image URL: \(randomAd.imageURL)")
        
        return randomAd
    }
}

// Example usage:
let adManager = AdvertisingManager()
adManager.addAdvertisement(title: "Game Promo", content: "Check out our new game!", imageURL: URL(string: "https://example.com/game.jpg")!)

if let displayedAd = adManager.displayAdvertisement() {
    // Do something with the displayed advertisement
    // For example, show it in your game
}
