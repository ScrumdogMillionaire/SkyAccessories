package com.bootcamp.skyapp;

/**
 * Created by tll01 on 27/07/2015.
 */
public class Product {

    private String name;
    private String pictureURL;
    private String price;
    private String description;
    private boolean available;

    public Product(String name, String pictureURL, String price, String description, boolean available){
        this.name = name;
        this.pictureURL = pictureURL;
        this.price = price;
        this.description = description;
        this.available = available;
    }

    public String getName(){
        return name;
    }

    public String getPictureURL(){
        return pictureURL;
    }

    public String getPrice() {
        return price;
    }

    public String getDescription() {
        return description;
    }

    public boolean isAvailable() {
        return available;
    }

}
