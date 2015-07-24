package com.bootcamp.skyapp;

import android.support.v4.app.FragmentActivity;
import android.os.Bundle;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

public class FindStore extends FragmentActivity {

    private GoogleMap mMap; // Might be null if Google Play services APK is not available.
    private Marker[] storeLocations;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_find_astore);
        setUpMapIfNeeded();
    }

    @Override
    protected void onResume() {
        super.onResume();
        setUpMapIfNeeded();
    }

    /**
     * Sets up the map if it is possible to do so (i.e., the Google Play services APK is correctly
     * installed) and the map has not already been instantiated.. This will ensure that we only ever
     * call {@link #setUpMap()} once when {@link #mMap} is not null.
     * <p/>
     * If it isn't installed {@link SupportMapFragment} (and
     * {@link com.google.android.gms.maps.MapView MapView}) will show a prompt for the user to
     * install/update the Google Play services APK on their device.
     * <p/>
     * A user can return to this FragmentActivity after following the prompt and correctly
     * installing/updating/enabling the Google Play services. Since the FragmentActivity may not
     * have been completely destroyed during this process (it is likely that it would only be
     * stopped or paused), {@link #onCreate(Bundle)} may not be called again so we should call this
     * method in {@link #onResume()} to guarantee that it will be called.
     */
    private void setUpMapIfNeeded() {
        // Do a null check to confirm that we have not already instantiated the map.
        if (mMap == null) {
            // Try to obtain the map from the SupportMapFragment.
            mMap = ((SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map))
                    .getMap();
            // Check if we were successful in obtaining the map.
            if (mMap != null) {
                setUpMap();
            }
        }
    }

    /**
     * This is where we can add markers or lines, add listeners or move the camera. In this case, we
     * just add a marker near Africa.
     * <p/>
     * This should only be called once and when we are sure that {@link #mMap} is not null.
     */
    private void setUpMap() {

        mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(new LatLng(54.437499, -2.384573), 6));

        storeLocations = populateLocations();

        for (int i = 0; i < storeLocations.length; i++) {
            mMap.addMarker(new MarkerOptions().position(new LatLng(storeLocations[i].getLatitude(), storeLocations[i].getLongitude())).title(storeLocations[i].getLocation()));
        }

    }

    private Marker[] populateLocations() {
        int numberOfLocations = 4;
        Marker[] locations = new Marker[numberOfLocations];

        locations[0] = new Marker(53.796590, -1.544412, "Trinity Leeds");
        locations[1] = new Marker(53.466085, -2.348114, "Trafford Center");
        locations[2] = new Marker(52.477747, -1.892496, "Bullring Shopping Center");
        locations[3] = new Marker(51.507453, -0.221144, "Westfield");

        return locations;
    }


}
