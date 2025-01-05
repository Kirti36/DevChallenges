package HotelBooking;

public class HotelApp {
    public static void main(String[] args) {
        // Create a hotel instance
        Hotel hotel = new Hotel();

        // Add rooms to the hotel
        int room1Number = hotel.addRoom("Single", 100.0, true);
        int room2Number = hotel.addRoom("Double", 150.0, false);
        
        // Book a room
        double bill = hotel.bookRoom(room1Number, "John Doe", "johndoe@example.com", 3);
        if (bill != -1) {
            System.out.println("Booking successful. Bill: $" + bill);
        } else {
            System.out.println("Room not available or already occupied.");
        }

        // Search for available rooms
        int availableSingleRooms = hotel.searchRoom("Single", true);
        System.out.println("Available single rooms with sea view: " + availableSingleRooms);

        int affordableRooms = hotel.searchRoom(120.0);
        System.out.println("Available rooms under $120 daily rent: " + affordableRooms);
    }
}

