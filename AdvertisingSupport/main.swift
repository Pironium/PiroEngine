import Foundation

class AdManager {
    static let shared = AdManager()
    
    private var ads: [Ad] = []
    
    func registerAd(ad: Ad) {
        ads.append(ad)
    }
    
    func showRandomAd() {
        guard let randomAd = ads.randomElement() else {
            print("No ads available")
            return
        }
        randomAd.show()
    }
}

protocol Ad {
    func show()
}

class BannerAd: Ad {
    let content: String
    
    init(content: String) {
        self.content = content
    }
    
    func show() {
        print("Showing banner ad with content: \(content)")
    }
}

class VideoAd: Ad {
    let duration: Int
    
    init(duration: Int) {
        self.duration = duration
    }
    
    func show() {
        print("Showing video ad with duration: \(duration) seconds")
    }
}
