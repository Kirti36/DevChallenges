package HotelBooking;
import java.util.ArrayList;
import java.util.List;

public class Hotel {
    private List<Room> rooms = new ArrayList<>();
    private int roomCounter = 101;

    public int addRoom(String roomType, double dailyRent, boolean seaView) {
        Room room = new Room(roomType, dailyRent, seaView);
        room.setRoomNumber(roomCounter++);
        rooms.add(room);
        return room.getRoomNumber();
    }

    public double bookRoom(int roomNumber, String guestName, String guestEmail, int numberOfDays) {
        for (Room room : rooms) {
            if (room.getRoomNumber() == roomNumber && !room.isOccupied()) {
                room.setOccupied(true);
                Booking booking = new Booking(roomNumber, guestName, guestEmail, numberOfDays);
                double bill = numberOfDays * room.getDailyRent();
                booking.setBill(bill);
                return bill;
            }
        }
        return -1; // Room not found or already occupied
    }

    public int searchRoom(String roomType, boolean seaView) {
        int count = 0;
        for (Room room : rooms) {
            if (!room.isOccupied() && room.getRoomType().equals(roomType) && room.isSeaView() == seaView) {
                count++;
            }
        }
        return count;
    }

    public int searchRoom(double maxDailyRent) {
        int count = 0;
        for (Room room : rooms) {
            if (!room.isOccupied() && room.getDailyRent() <= maxDailyRent) {
                count++;
            }
        }
        return count;
    }
}    

