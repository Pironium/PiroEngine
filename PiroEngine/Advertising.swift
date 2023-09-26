import Foundation

// Define an enum to represent different types of ads
enum AdType {
    case banner
    case interstitial
    case rewarded
}

// Create a struct to store ad information
struct Ad {
    let adType: AdType
    let adID: String
    let adContent: String
}

// Class to manage ads in PiroEngine
class AdvertisingManager {
    // Store ads in an array
    private var ads: [Ad] = []
    
    // Function to add a new ad to the system
    func addAd(adType: AdType, adID: String, adContent: String) {
        let newAd = Ad(adType: adType, adID: adID, adContent: adContent)
        ads.append(newAd)
    }
    
    // Function to display an ad based on ad type
    func displayAd(adType: AdType) {
        switch adType {
        case .banner:
            print("Displaying banner ad")
            // Code to display a banner ad
        case .interstitial:
            print("Displaying interstitial ad")
            // Code to display an interstitial ad
        case .rewarded:
            print("Displaying rewarded ad")
            // Code to display a rewarded ad
        }
    }
    
    // Function to remove an ad from the system
    func removeAd(adID: String) {
        ads.removeAll { $0.adID == adID }
    }
    
    // Function to check if an ad exists in the system
    func adExists(adID: String) -> Bool {
        return ads.contains { $0.adID == adID }
    }
}
