package HotelBooking;

public class Room {
    private String roomType;
    private double dailyRent;
    private boolean seaView;
    private int roomNumber;
    private boolean isOccupied;

    public Room(String roomType, double dailyRent, boolean seaView) {
        this.roomType = roomType;
        this.dailyRent = dailyRent;
        this.seaView = seaView;
        this.isOccupied = false;
    }

    // Getters and setters for Room class
    public String getRoomType() {
        return roomType;
    }

    public void setRoomType(String roomType) {
        this.roomType = roomType;
    }

    public double getDailyRent() {
        return dailyRent;
    }

    public void setDailyRent(double dailyRent) {
        this.dailyRent = dailyRent;
    }

    public boolean isSeaView() {
        return seaView;
    }

    public void setSeaView(boolean seaView) {
        this.seaView = seaView;
    }

    public int getRoomNumber() {
        return roomNumber;
    }

    public void setRoomNumber(int roomNumber) {
        this.roomNumber = roomNumber;
    }

    public boolean isOccupied() {
        return isOccupied;
    }

    public void setOccupied(boolean occupied) {
        isOccupied = occupied;
    }
}


    
