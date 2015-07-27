package com.bootcamp.skyapp;

import android.app.IntentService;
import android.content.Intent;
import android.content.Context;

import com.google.android.gms.location.Geofence;
import com.google.android.gms.location.GeofencingEvent;

import java.util.List;


public class NotificationService extends IntentService {

    public NotificationService() {
        super("NotificationService");
    }

    @Override
    protected void onHandleIntent(Intent intent) {
        if (intent != null) {
            GeofencingEvent geofencingEvent = GeofencingEvent.fromIntent(intent);
            List<Geofence> triggeringGeofences = geofencingEvent.getTriggeringGeofences();

            Geofence triggeredStore = triggeringGeofences.get(0);

            NotificationLauncher.fireNotification(this, triggeredStore.getRequestId(), "Visit today and get 10% off!", FindStore.class);
            //this.stopSelf();
        }
    }


}
