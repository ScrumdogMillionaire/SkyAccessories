package com.bootcamp.skyapp;

/**
 * Created by tll01 on 27/07/2015.
 */
public class Product {

    private String name;
    private String pictureURL;

    public Product(String name, String pictureURL){
        this.name = name;
        this.pictureURL = pictureURL;
    }

    public String getName(){
        return name;
    }

    public String getPictureURL(){
        return pictureURL;
    }

}
