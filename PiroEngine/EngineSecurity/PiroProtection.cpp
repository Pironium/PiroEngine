#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <stdexcept>
#include <ctime>

// Define a structure to represent a license key
struct LicenseKey {
    std::string key;
    time_t expirationDate;
};

// Define a class to manage license keys and piracy protection
class PiroProtection {
private:
    std::unordered_map<std::string, LicenseKey> licenseKeys;

public:
    // Constructor to initialize the PiroProtection module
    PiroProtection() {
        // Load predefined license keys from a secure source
        loadLicenseKeys();
    }

    // Function to generate a new unique license key
    std::string generateLicenseKey(std::string gameName, int validityDays) {
        // Generate a unique key based on game name and current time
        std::string key = gameName + "_" + std::to_string(std::time(nullptr));
        
        // Create a LicenseKey struct with the generated key and expiration date
        LicenseKey newKey;
        newKey.key = key;
        newKey.expirationDate = std::time(nullptr) + validityDays * 24 * 60 * 60; // Validity in seconds
        
        // Store the key in the map
        licenseKeys[key] = newKey;
        
        return key;
    }

    // Function to verify the validity of a given license key
    bool verifyLicenseKey(std::string key) {
        if (licenseKeys.find(key) != licenseKeys.end()) {
            LicenseKey& license = licenseKeys[key];
            time_t currentTime = std::time(nullptr);
            if (license.expirationDate >= currentTime) {
                // Key is valid and not expired
                return true;
            }
        }
        return false;
    }

    // Function to revoke a license key
    void revokeLicenseKey(std::string key) {
        if (licenseKeys.find(key) != licenseKeys.end()) {
            licenseKeys.erase(key);
        }
    }

    // Function to load predefined license keys (e.g., from a secure file)
    void loadLicenseKeys() {
        // In a real-world scenario, load keys from a secure source like a database or file
        // For the sake of this example, we'll add some predefined keys
        generateLicenseKey("Game1", 365); // Valid for 1 year
        generateLicenseKey("Game2", 180); // Valid for 6 months
        generateLicenseKey("Game3", 30);  // Valid for 1 month
    }
};

int main() {
    PiroProtection piracyProtection;

    // Generate a new license key for a game
    std::string newLicenseKey = piracyProtection.generateLicenseKey("NewGame", 90);

    // Verify the validity of a license key
    if (piracyProtection.verifyLicenseKey(newLicenseKey)) {
        std::cout << "License key is valid." << std::endl;
    } else {
        std::cout << "License key is invalid or expired." << std::endl;
    }

    // Revoke a license key (e.g., if it's suspected of being pirated)
    piracyProtection.revokeLicenseKey(newLicenseKey);

    return 0;
}
