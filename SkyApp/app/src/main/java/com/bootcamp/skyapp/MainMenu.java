package com.bootcamp.skyapp;

import android.animation.Animator;
import android.animation.AnimatorListenerAdapter;
import android.animation.AnimatorSet;
import android.animation.ObjectAnimator;
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
import android.view.animation.AnticipateInterpolator;
import android.view.animation.OvershootInterpolator;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.common.api.ResultCallback;
import com.google.android.gms.common.api.Status;
import com.google.android.gms.location.Geofence;
import com.google.android.gms.location.GeofencingRequest;
import com.google.android.gms.location.LocationServices;
import com.ogaclejapan.arclayout.ArcLayout;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.List;


public class MainMenu extends Activity {

    private boolean curVisible = false;
    private View menuLayout;
    private ArcLayout arcLayout;
    private ImageView fab;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        String fontPath = "skymed.ttf";
        Typeface tf = Typeface.createFromAsset(getAssets(), fontPath);

        TextView hello = (TextView) findViewById(R.id.hello);
        hello.setTypeface(tf);
        hello.setText("Hi " + User.getInstance().getFirstName() + ". You have");

        TextView points = (TextView) findViewById(R.id.points);
        points.setTypeface(tf);
        points.setText(User.getInstance().getPoints() + " points");

        menuLayout = findViewById(R.id.menu_layout);
        arcLayout = (ArcLayout) findViewById(R.id.arc_layout);
        fab = (ImageView) findViewById(R.id.fab);
    }

    @Override
    protected void onResume() {
        super.onResume();

        Log.d("Points on main page: ", User.getInstance().getPoints() + "");

        TextView points = (TextView) findViewById(R.id.points);
        points.setText(User.getInstance().getPoints() + " points");
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_menu, menu);
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

    public void toggleLayout(final View v){
        if (!curVisible){
            menuLayout.setVisibility(View.VISIBLE);

            List<Animator> animList = new ArrayList<>();

            for (int i = 0, len = arcLayout.getChildCount(); i < len; i++) {
                animList.add(createShowItemAnimator(arcLayout.getChildAt(i)));
            }

            AnimatorSet animSet = new AnimatorSet();
            animSet.setDuration(400);
            animSet.setInterpolator(new OvershootInterpolator());
            animSet.playTogether(animList);
            animSet.start();

            fab.setBackgroundResource(R.drawable.pause);
            curVisible = true;
        } else {
            List<Animator> animList = new ArrayList<>();

            for (int i = arcLayout.getChildCount() - 1; i >= 0; i--) {
                animList.add(createHideItemAnimator(arcLayout.getChildAt(i)));
            }

            AnimatorSet animSet = new AnimatorSet();
            animSet.setDuration(400);
            animSet.setInterpolator(new AnticipateInterpolator());
            animSet.playTogether(animList);
            animSet.addListener(new AnimatorListenerAdapter() {
                @Override
                public void onAnimationEnd(Animator animation) {
                    super.onAnimationEnd(animation);
                    menuLayout.setVisibility(View.INVISIBLE);

                    switch(v.getId()) {
                        case R.id.reward:
                            loadActivity(RedeemReward.class);
                            break;
                        case R.id.account:
                            loadActivity(AccountPage.class);
                            break;
                        case R.id.location:
                            loadActivity(FindStore.class);
                            break;
                        case R.id.info:
                            loadActivity(InfoActivity.class);
                            break;
                        case R.id.logout:
                            loadActivity(LandingActivity.class);
                    }

                }
            });
            animSet.start();

            fab.setBackgroundResource(R.drawable.middle);
            curVisible = false;
        }
    }


    private Animator createShowItemAnimator(View item) {

        float dx = fab.getX() - item.getX();
        float dy = fab.getY() - item.getY();

        item.setRotation(0f);
        item.setTranslationX(dx);
        item.setTranslationY(dy);

        Animator anim = ObjectAnimator.ofPropertyValuesHolder(
                item,
                AnimatorUtils.rotation(0f, 720f),
                AnimatorUtils.translationX(dx, 0f),
                AnimatorUtils.translationY(dy, 0f)
        );

        return anim;
    }

    private Animator createHideItemAnimator(final View item) {
        float dx = fab.getX() - item.getX();
        float dy = fab.getY() - item.getY();

        Animator anim = ObjectAnimator.ofPropertyValuesHolder(
                item,
                AnimatorUtils.rotation(720f, 0f),
                AnimatorUtils.translationX(0f, dx),
                AnimatorUtils.translationY(0f, dy)
        );

        anim.addListener(new AnimatorListenerAdapter() {
            @Override
            public void onAnimationEnd(Animator animation) {
                super.onAnimationEnd(animation);
                item.setTranslationX(0f);
                item.setTranslationY(0f);
            }
        });

        return anim;
    }

    public void loadLocation(View v){
        Intent resultIntent = new Intent(this, FindStore.class);
        toggleLayout(v);

        startActivity(resultIntent);
    }

    public void loadActivity(Class<?> activity) {
        Intent resultIntent = new Intent(this, activity);

        if (activity == LandingActivity.class){ //Logout
            resultIntent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_NEW_TASK);

            try {
                //Opens and closes user login status (/Empties file)
                openFileOutput("userstate", Context.MODE_PRIVATE).close();
            } catch (Exception e){
                e.printStackTrace();
            }
        }

        startActivity(resultIntent);
    }
}
