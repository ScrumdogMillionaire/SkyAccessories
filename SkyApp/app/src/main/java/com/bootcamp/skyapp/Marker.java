package com.bootcamp.skyapp;

/**
 * Created by tll01 on 24/07/2015.
 */
public class Marker {
    private double latitude;
    private double longitude;
    private String location;

    public Marker(double latitude, double longitude, String location) {
        this.latitude = latitude;
        this.longitude = longitude;
        this.location = "Sky Store, " + location;
    }

    public double getLatitude() {
        return latitude;
    }

    public void setLatitude(double latitude) {
        this.latitude = latitude;
    }

    public double getLongitude() {
        return longitude;
    }

    public void setLongitude(double longitude) {
        this.longitude = longitude;
    }

    public String getLocationDescription() {
        return location;
    }

    public void setLocation(String location) {
        this.location = "Sky Store, " + location;
    }
}

