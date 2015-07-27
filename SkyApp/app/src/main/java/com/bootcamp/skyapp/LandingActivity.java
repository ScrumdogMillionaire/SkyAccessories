package com.bootcamp.skyapp;

import android.app.Activity;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.support.v4.app.NotificationCompat;
import android.support.v4.app.TaskStackBuilder;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.Window;

import org.json.JSONArray;
import org.json.JSONException;

import java.util.ArrayList;
import java.util.concurrent.ExecutionException;


public class LandingActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_landing);

        //AsyncTask task = new RetrieveJSON().execute("http://192.168.1.21:3001/skystore/api/orders/");

        ArrayList<Marker> markers = RetrieveJSON.getMarkers();

        for (Marker store : markers) {
            Log.d("Store Latitude: ", ""+store.getLatitude());
            Log.d("Store Longitude: ", ""+store.getLongitude());
            Log.d("Store Description: ", store.getLocationDescription());
        }

        this.startService(new Intent(this, GeofenceService.class));

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_landing, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    public void loadLogin(View v){
        Intent resultIntent = new Intent(this, Login.class);
        startActivity(resultIntent);
    }

    public void loadSignup(View v){
        Intent resultIntent = new Intent(this, Signup.class);
        startActivity(resultIntent);
    }
}
