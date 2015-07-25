package com.bootcamp.skyapp;

import android.app.Activity;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.graphics.Typeface;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.common.api.ResultCallback;
import com.google.android.gms.common.api.Status;
import com.google.android.gms.location.Geofence;
import com.google.android.gms.location.GeofencingRequest;
import com.google.android.gms.location.LocationServices;

import java.util.ArrayList;


public class MainMenu extends Activity {

    ArrayList<Geofence> mGeofenceList = new ArrayList<Geofence>();
    GoogleApiClient mGoogleApiClient;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);


        String fontPath = "skymed.ttf";
        TextView txtGhost = (TextView) findViewById(R.id.helloUser);
        Button redeemReward = (Button) findViewById(R.id.actionRedeem);
        Typeface tf = Typeface.createFromAsset(getAssets(), fontPath);
        txtGhost.setTypeface(tf);
        redeemReward.setTypeface(tf);

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
