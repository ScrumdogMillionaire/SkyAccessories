package com.bootcamp.skyapp;

import java.io.Serializable;

/**
 * Created by tll01 on 29/07/2015.
 */
public class User implements Serializable {
    private String token;
    private String id;
    private int points;
    private String email;
    private String username;
    private String firstName;
    private String lastName;
    private static User user;

    public static User getInstance() {
        return user;
    }

    public static void makeUser(String token, String id, int points, String email, String username, String firstName, String lastName) {
        user = new User(token, id, points, email, username, firstName, lastName);
    }

    private User(String token, String id, int points, String email, String username, String firstName, String lastName){
        this.token = token;
        this.id = id;
        this.points = points;
        this.email = email;
        this.username = username;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
}
