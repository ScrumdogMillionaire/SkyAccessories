package com.bootcamp.skyapp;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;

import com.google.android.gms.location.Geofence;

import java.util.ArrayList;


public class MainMenu extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        ArrayList<Geofence> mGeofenceList = new ArrayList<Geofence>();

        mGeofenceList.add(new Geofence.Builder()
                // Set the request ID of the geofence. This is a string to identify this
                // geofence.
                .setRequestId("1")

                .setCircularRegion(
                        53.796676,
                        -1.544610,
                        100
                )
                .setExpirationDuration(10)
                .setTransitionTypes(Geofence.GEOFENCE_TRANSITION_ENTER |
                        Geofence.GEOFENCE_TRANSITION_EXIT)
                .build());

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menuActivity) {
        // Inflate the menuActivity; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_menu, menuActivity);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    public void loadRedeemReward(View v){
        Intent resultIntent = new Intent(this, RedeemReward.class);
        startActivity(resultIntent);
    }

    public void loadLocalStore(View v){
        Intent resultIntent = new Intent(this, FindStore.class);
        startActivity(resultIntent);
    }

    public void loadAccount(View v){
        Intent resultIntent = new Intent(this, AccountPage.class);
        startActivity(resultIntent);
    }
}
