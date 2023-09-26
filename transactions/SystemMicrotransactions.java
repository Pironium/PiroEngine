import java.util.HashMap;
import java.util.Map;

public class SystemMicrotransactions {
    private Map<String, Double> itemPrices;

    public SystemMicrotransactions() {
        this.itemPrices = new HashMap<>();
        initializeItemPrices();
    }

    private void initializeItemPrices() {
        itemPrices.put("SwordSkin", 4.99);
        itemPrices.put("HealthPotion", 2.49);
        itemPrices.put("MagicScroll", 3.99);
        // Add more items and prices as needed
    }

    public double getItemPrice(String itemName) {
        if (itemPrices.containsKey(itemName)) {
            return itemPrices.get(itemName);
        } else {
            System.out.println("Item not found.");
            return 0.0;
        }
    }

    public boolean processTransaction(String itemName, String paymentMethod, String paymentDetails) {
        // Logic to process the transaction using the provided payment method and details
        // This can include payment gateways, validations, and updating user's inventory
        System.out.println("Processing transaction for item: " + itemName);
        System.out.println("Payment method: " + paymentMethod);
        System.out.println("Payment details: " + paymentDetails);

        // Placeholder return, assuming transaction is always successful for the sake of example
        return true;
    }
}
